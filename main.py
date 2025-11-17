import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pykrx")
import sys
import qdarkstyle
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QVBoxLayout
from PySide6.QtCore import QDate
from main_ui import Ui_MainWindow
from pykrx import stock
import datetime
import pandas as pd
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

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
        self.ui.listWidgetStocks.currentItemChanged.connect(self.update_stock_history)
        # Connect pushButtonReload to update_stock_history
        self.ui.pushButtonReload.clicked.connect(self.update_stock_history)

        # Create plot canvases
        self.price_canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.ui.verticalLayoutPlotPrice.addWidget(self.price_canvas)
        self.amount_canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.ui.verticalLayoutPlotAmout.addWidget(self.amount_canvas)

    def close_application(self):
        self.close()

    def update_stock_history(self):
        current_item = self.ui.listWidgetStocks.currentItem()
        if current_item is None:
            return

        selected_market = self.ui.comboBoxMarket.currentText()
        if selected_market not in ["KOSPI", "KOSDAQ"]:
            self.ui.tableWidgetHistory.clear()
            self.ui.tableWidgetHistory.setRowCount(0)
            self.ui.tableWidgetHistory.setColumnCount(0)
            self.price_canvas.axes.cla()
            self.price_canvas.draw()
            self.amount_canvas.axes.cla()
            self.amount_canvas.draw()
            return

        # Extract ticker from the selected item
        ticker = current_item.text().split("(")[-1].replace(")", "")

        # Get start and end dates
        start_date = self.ui.dateEditStart.date().toString("yyyyMMdd")
        end_date = self.ui.dateEditEnd.date().toString("yyyyMMdd")

        # Fetch stock history
        try:
            df = stock.get_market_ohlcv(start_date, end_date, ticker)
            self.populate_history_table(df)
            self.plot_stock_data(df)
        except Exception as e:
            print(f"Error fetching stock history: {e}")
            self.ui.tableWidgetHistory.clear()
            self.ui.tableWidgetHistory.setRowCount(0)
            self.ui.tableWidgetHistory.setColumnCount(0)

    def plot_stock_data(self, df):
        # Plot price
        self.price_canvas.axes.cla()
        self.price_canvas.axes.plot(df.index, df['종가'])
        self.price_canvas.axes.set_title("Price")
        self.price_canvas.draw()

        # Plot volume
        self.amount_canvas.axes.cla()
        self.amount_canvas.axes.bar(df.index, df['거래량'])
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
                df = pd.read_csv("nyse-listed.csv")
                for index, row in df.iterrows():
                    self.ui.listWidgetStocks.addItem(f"{row['Company Name']} ({row['ACT Symbol']})")
            except FileNotFoundError:
                self.ui.listWidgetStocks.addItem("nyse-listed.csv not found.")
        elif selected_market == "NASDAQ":
            try:
                df = pd.read_csv("nasdaq-listed.csv")
                for index, row in df.iterrows():
                    self.ui.listWidgetStocks.addItem(f"{row['Security Name']} ({row['Symbol']})")
            except FileNotFoundError:
                self.ui.listWidgetStocks.addItem("nasdaq-listed.csv not found.")


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
