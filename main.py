import sys
import qdarkstyle
from PySide6.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow
from pykrx import stock
import datetime
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBoxMarket.currentIndexChanged.connect(self.update_stock_list)
        # Initial call to populate the list when the app starts
        self.update_stock_list()

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
