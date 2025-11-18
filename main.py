import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pykrx")
import sys
import qdarkstyle
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QVBoxLayout
from PySide6.QtCore import QDate, QThread, Signal
from main_ui import Ui_MainWindow
from pykrx import stock
import datetime
import pandas as pd
import yfinance as yf
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import json

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Worker(QThread):
    finished = Signal(object)

    def __init__(self, market, period):
        super().__init__()
        self.market = market
        self.period = period

    def run(self):
        today = datetime.datetime.now()
        if self.period == "1 Day":
            start_date = today - datetime.timedelta(days=1)
        elif self.period == "1 Week":
            start_date = today - datetime.timedelta(weeks=1)
        elif self.period == "1 Month":
            start_date = today - datetime.timedelta(days=30)
        else:
            start_date = today - datetime.timedelta(days=1)

        start_date_str = start_date.strftime("%Y-%m-%d")
        end_date_str = today.strftime("%Y-%m-%d")

        results = []
        if self.market in ["KOSPI", "KOSDAQ"]:
            tickers = stock.get_market_ticker_list(today.strftime("%Y%m%d"), market=self.market)
            for ticker in tickers[:20]: # Limiting for performance
                try:
                    df = stock.get_market_ohlcv(start_date.strftime("%Y%m%d"), today.strftime("%Y%m%d"), ticker)
                    if not df.empty:
                        price_change = (df['종가'].iloc[-1] - df['종가'].iloc[0]) / df['종가'].iloc[0] * 100
                        name = stock.get_market_ticker_name(ticker)
                        results.append((name, ticker, price_change))
                except Exception as e:
                    print(f"Error fetching {ticker}: {e}")
        elif self.market in ["NYSE", "NASDAQ"]:
            if self.market == "NYSE":
                csv_file = "nyse-listed.csv"
                symbol_col = "ACT Symbol"
                name_col = "Company Name"
            else:
                csv_file = "nasdaq-listed.csv"
                symbol_col = "Symbol"
                name_col = "Security Name"
            try:
                df_tickers = pd.read_csv(csv_file).dropna(subset=[symbol_col, name_col])
                # Filter out tickers with non-alphanumeric characters, keeping only uppercase letter tickers
                df_tickers = df_tickers[df_tickers[symbol_col].str.match(r'^[A-Z]+$')]
                
                # Keep fetching until we have 20 results or have tried all tickers
                while len(results) < 20 and not df_tickers.empty:
                    sample_size = min(100, len(df_tickers))
                    for index, row in df_tickers.sample(n=sample_size).iterrows():
                        ticker = row[symbol_col]
                        name = row[name_col]
                        
                        # Remove the ticker from the list to avoid re-fetching
                        df_tickers = df_tickers.drop(index)

                        try:
                            ticker_obj = yf.Ticker(ticker)
                            df = ticker_obj.history(start=start_date_str, end=end_date_str)
                            if not df.empty and 'Close' in df.columns and not df['Close'].isnull().all():
                                if len(df['Close']) > 1:
                                    price_change = (df['Close'].iloc[-1] - df['Close'].iloc[0]) / df['Close'].iloc[0] * 100
                                    results.append((name, ticker, price_change))
                                    if len(results) >= 20:
                                        break 
                                else:
                                    print(f"Not enough data for {ticker} to calculate change.")
                            else:
                                print(f"No data for {ticker}, possibly delisted.")
                        except Exception as e:
                            print(f"Failed to get ticker '{ticker}' reason: {e}")
                    if len(results) >= 20:
                        break
            except FileNotFoundError:
                print(f"{csv_file} not found.")

        results.sort(key=lambda x: x[2])
        self.finished.emit(results)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBoxMarket.currentIndexChanged.connect(self.update_stock_list)
        # Initial call to populate the list when the app starts
        self.update_stock_list()

        # Connect actionExit to close the application
        self.ui.actionExit.triggered.connect(self.close_application)

        # Set dateEditEnd to today's date
        self.ui.dateEditEnd.setDate(QDate.currentDate())

        # Set dateEditStart to today minus one year
        self.ui.dateEditStart.setDate(QDate.currentDate().addYears(-1))

        # Connect listWidgetStocks to update_stock_history
        self.ui.listWidgetStocks.currentItemChanged.connect(lambda: self.update_stock_history(self.ui.listWidgetStocks))
        # Connect pushButtonReload to update_stock_history
        self.ui.pushButtonReload.clicked.connect(self.reload_active_stock_history)

        # Connect listWidgetSelectedTickers to update_stock_history
        self.ui.listWidgetSelectedTickers.currentItemChanged.connect(lambda: self.update_stock_history(self.ui.listWidgetSelectedTickers))

        # Connect lineEditKeyWord to filter_stock_list
        self.ui.lineEditKeyWord.textChanged.connect(self.filter_stock_list)

        # Create plot canvases
        self.price_canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.ui.verticalLayoutPlotPrice.addWidget(self.price_canvas)
        self.amount_canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.ui.verticalLayoutPlotAmout.addWidget(self.amount_canvas)

        # Connect comboBoxPeriod to period_changed
        self.ui.comboBoxPeriod.currentIndexChanged.connect(self.period_changed)

        # Connect pushButtonAddSelected to add_selected_ticker
        self.ui.pushButtonAddSelected.clicked.connect(self.add_selected_ticker)

        # Connect pushButtonRemoveSelected to remove_selected_ticker
        self.ui.pushButtonRemoveSelected.clicked.connect(self.remove_selected_ticker)

        # Setup for Top Decliners tab
        if hasattr(self.ui, 'pushButtonFindDecliners'):
            self.ui.pushButtonFindDecliners.clicked.connect(self.find_top_decliners)
            self.ui.comboBoxDeclinersPeriod.addItems(["1 Day", "1 Week", "1 Month"])

        # Load selected tickers from file
        self.load_selected_tickers()

    def save_selected_tickers(self):
        items = []
        for i in range(self.ui.listWidgetSelectedTickers.count()):
            items.append(self.ui.listWidgetSelectedTickers.item(i).text())
        with open("selected.json", "w") as f:
            json.dump(items, f)

    def load_selected_tickers(self):
        try:
            with open("selected.json", "r") as f:
                items = json.load(f)
                self.ui.listWidgetSelectedTickers.addItems(items)
        except FileNotFoundError:
            pass # No file to load

    def add_selected_ticker(self):
        current_item = self.ui.listWidgetStocks.currentItem()
        if current_item:
            item_text = current_item.text()
            # Check if the item already exists in listWidgetSelectedTickers
            for i in range(self.ui.listWidgetSelectedTickers.count()):
                if self.ui.listWidgetSelectedTickers.item(i).text() == item_text:
                    return # Item already exists, do not add
            self.ui.listWidgetSelectedTickers.addItem(item_text)
            self.save_selected_tickers()

    def remove_selected_ticker(self):
        current_item = self.ui.listWidgetSelectedTickers.currentItem()
        if current_item:
            self.ui.listWidgetSelectedTickers.takeItem(self.ui.listWidgetSelectedTickers.row(current_item))
            self.save_selected_tickers()

    def find_top_decliners(self):
        market = self.ui.comboBoxMarket.currentText()
        period = self.ui.comboBoxDeclinersPeriod.currentText()
        self.worker = Worker(market, period)
        self.worker.finished.connect(self.update_decliners_table)
        self.worker.start()
        if hasattr(self.ui, 'pushButtonFindDecliners'):
            self.ui.pushButtonFindDecliners.setText("Loading...")
            self.ui.pushButtonFindDecliners.setEnabled(False)

    def update_decliners_table(self, results):
        if hasattr(self.ui, 'tableWidgetDecliners'):
            self.ui.tableWidgetDecliners.clear()
            self.ui.tableWidgetDecliners.setRowCount(len(results))
            self.ui.tableWidgetDecliners.setColumnCount(3)
            self.ui.tableWidgetDecliners.setHorizontalHeaderLabels(["Name", "Ticker", "Change (%)"])
            for i, (name, ticker, change) in enumerate(results):
                self.ui.tableWidgetDecliners.setItem(i, 0, QTableWidgetItem(name))
                self.ui.tableWidgetDecliners.setItem(i, 1, QTableWidgetItem(ticker))
                self.ui.tableWidgetDecliners.setItem(i, 2, QTableWidgetItem(f"{change:.2f}%"))
        if hasattr(self.ui, 'pushButtonFindDecliners'):
            self.ui.pushButtonFindDecliners.setText("Find Decliners")
            self.ui.pushButtonFindDecliners.setEnabled(True)

    def reload_active_stock_history(self):
        if self.ui.tabWidget_2.currentWidget() == self.ui.tabSelected:
            current_list_widget = self.ui.listWidgetSelectedTickers
        else:
            current_list_widget = self.ui.listWidgetStocks
        self.update_stock_history(current_list_widget)

    def period_changed(self):
        period = self.ui.comboBoxPeriod.currentText()
        end_date = QDate.currentDate()
        self.ui.dateEditEnd.setDate(end_date)

        if period == "Custom":
            self.ui.dateEditStart.setEnabled(True)
            self.ui.dateEditEnd.setEnabled(True)
            return
        else:
            self.ui.dateEditStart.setEnabled(False)
            self.ui.dateEditEnd.setEnabled(False)

        if period == "1 Year":
            start_date = end_date.addYears(-1)
        elif period == "6 Months":
            start_date = end_date.addMonths(-6)
        elif period == "1 Month" or period == "1 Months":
            start_date = end_date.addMonths(-1)
        elif period == "2 Weeks":
            start_date = end_date.addDays(-14)
        elif period == "1 Week":
            start_date = end_date.addDays(-7)
        else:
            return

        self.ui.dateEditStart.setDate(start_date)
        self.reload_active_stock_history()

    def filter_stock_list(self):
        keyword = self.ui.lineEditKeyWord.text().lower()
        for i in range(self.ui.listWidgetStocks.count()):
            item = self.ui.listWidgetStocks.item(i)
            item.setHidden(keyword not in item.text().lower())

    def close_application(self):
        self.close()

    def update_stock_history(self, list_widget):
        if list_widget is None:
            return

        current_item = list_widget.currentItem()
        if current_item is None:
            return

        selected_market = self.ui.comboBoxMarket.currentText()
        ticker = current_item.text().split("(")[-1].replace(")", "")
        start_date = self.ui.dateEditStart.date().toString("yyyy-MM-dd")
        end_date = self.ui.dateEditEnd.date().toString("yyyy-MM-dd")

        try:
            df = None
            if selected_market in ["KOSPI", "KOSDAQ"]:
                df = stock.get_market_ohlcv(self.ui.dateEditStart.date().toString("yyyyMMdd"), self.ui.dateEditEnd.date().toString("yyyyMMdd"), ticker)
            elif selected_market in ["NYSE", "NASDAQ"]:
                ticker_obj = yf.Ticker(ticker)
                df = ticker_obj.history(start=start_date, end=end_date)
                if df.empty:
                    print(f"No history for {ticker}, possibly delisted.")
                    
            if df is not None and not df.empty:
                self.populate_history_table(df)
                self.plot_stock_data(df, selected_market)
            else:
                # Clear table and plots if no data is found
                self.ui.tableWidgetHistory.clear()
                self.ui.tableWidgetHistory.setRowCount(0)
                self.ui.tableWidgetHistory.setColumnCount(0)
                self.price_canvas.axes.cla()
                self.price_canvas.draw()
                self.amount_canvas.axes.cla()
                self.amount_canvas.draw()

        except Exception as e:
            print(f"Error fetching stock history for {ticker}: {e}")
            self.ui.tableWidgetHistory.clear()
            self.ui.tableWidgetHistory.setRowCount(0)
            self.ui.tableWidgetHistory.setColumnCount(0)
            self.price_canvas.axes.cla()
            self.price_canvas.draw()
            self.amount_canvas.axes.cla()
            self.amount_canvas.draw()

    def plot_stock_data(self, df, market):
        price_col = '종가' if market in ["KOSPI", "KOSDAQ"] else 'Close'
        volume_col = '거래량' if market in ["KOSPI", "KOSDAQ"] else 'Volume'

        # Plot price
        self.price_canvas.axes.cla()
        self.price_canvas.axes.plot(df.index, df[price_col], label='Price')
        
        # Calculate and plot moving averages
        if len(df) >= 20:
            ma20 = df[price_col].rolling(window=20).mean()
            self.price_canvas.axes.plot(df.index, ma20, label='20-Day MA')
        if len(df) >= 50:
            ma50 = df[price_col].rolling(window=50).mean()
            self.price_canvas.axes.plot(df.index, ma50, label='50-Day MA')
            
        self.price_canvas.axes.set_title("Price")
        self.price_canvas.axes.legend()
        self.price_canvas.draw()

        # Plot volume
        self.amount_canvas.axes.cla()
        self.amount_canvas.axes.bar(df.index, df[volume_col])
        self.amount_canvas.axes.set_title("Volume")
        self.amount_canvas.draw()

    def populate_history_table(self, df):
        self.ui.tableWidgetHistory.clear()
        
        # Add 'Date' as the first column header
        headers = ["Date"] + list(df.columns)
        self.ui.tableWidgetHistory.setColumnCount(len(headers))
        self.ui.tableWidgetHistory.setHorizontalHeaderLabels(headers)
        self.ui.tableWidgetHistory.setRowCount(len(df))

        for i, (index, row) in enumerate(df.iterrows()):
            # Set the date in the first column
            self.ui.tableWidgetHistory.setItem(i, 0, QTableWidgetItem(str(index.strftime("%Y-%m-%d"))))
            # Set the rest of the data in subsequent columns
            for j, col in enumerate(df.columns):
                self.ui.tableWidgetHistory.setItem(i, j + 1, QTableWidgetItem(str(row[col])))

    def update_stock_list(self):
        selected_market = self.ui.comboBoxMarket.currentText()
        self.ui.listWidgetStocks.clear()

        if selected_market in ["KOSPI", "KOSDAQ"]:
            today = datetime.datetime.now().strftime("%Y%m%d")
            tickers = stock.get_market_ticker_list(today, market=selected_market)
            for ticker in tickers:
                name = stock.get_market_ticker_name(ticker)
                self.ui.listWidgetStocks.addItem(f"{name} ({ticker})")
        elif selected_market == "NYSE":
            try:
                df = pd.read_csv("nyse-listed.csv").dropna(subset=["ACT Symbol", "Company Name"])
                df = df[df["ACT Symbol"].str.match(r'^[A-Z]+$')]
                for index, row in df.iterrows():
                    self.ui.listWidgetStocks.addItem(f"{row['Company Name']} ({row['ACT Symbol']})")
            except FileNotFoundError:
                self.ui.listWidgetStocks.addItem("nyse-listed.csv not found.")
        elif selected_market == "NASDAQ":
            try:
                df = pd.read_csv("nasdaq-listed.csv").dropna(subset=["Symbol", "Security Name"])
                df = df[df["Symbol"].str.match(r'^[A-Z]+$')]
                for index, row in df.iterrows():
                    self.ui.listWidgetStocks.addItem(f"{row['Security Name']} ({row['Symbol']})")
            except FileNotFoundError:
                self.ui.listWidgetStocks.addItem("nasdaq-listed.csv not found.")


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
    window = MainWindow()
    
    # Gracefully terminate the worker thread on application exit
    def cleanup():
        if hasattr(window, 'worker') and window.worker.isRunning():
            window.worker.terminate()
            window.worker.wait() # Wait for the thread to finish
    
    app.aboutToQuit.connect(cleanup)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
