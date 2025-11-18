# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1465, 952)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(250, 0))
        self.frame_4.setMaximumSize(QSize(250, 16777215))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBoxMarket = QComboBox(self.frame_4)
        self.comboBoxMarket.addItem("")
        self.comboBoxMarket.addItem("")
        self.comboBoxMarket.addItem("")
        self.comboBoxMarket.addItem("")
        self.comboBoxMarket.setObjectName(u"comboBoxMarket")

        self.verticalLayout_2.addWidget(self.comboBoxMarket)

        self.listWidgetStocks = QListWidget(self.frame_4)
        self.listWidgetStocks.setObjectName(u"listWidgetStocks")

        self.verticalLayout_2.addWidget(self.listWidgetStocks)

        self.lineEditKeyWord = QLineEdit(self.frame_4)
        self.lineEditKeyWord.setObjectName(u"lineEditKeyWord")

        self.verticalLayout_2.addWidget(self.lineEditKeyWord)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label)

        self.dateEditStart = QDateEdit(self.frame_2)
        self.dateEditStart.setObjectName(u"dateEditStart")
        self.dateEditStart.setDateTime(QDateTime(QDate(2023, 12, 31), QTime(15, 0, 0)))

        self.horizontalLayout_2.addWidget(self.dateEditStart)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.dateEditEnd = QDateEdit(self.frame_2)
        self.dateEditEnd.setObjectName(u"dateEditEnd")
        self.dateEditEnd.setDateTime(QDateTime(QDate(2024, 12, 31), QTime(15, 0, 0)))

        self.horizontalLayout_2.addWidget(self.dateEditEnd)

        self.comboBoxPeriod = QComboBox(self.frame_2)
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.setObjectName(u"comboBoxPeriod")

        self.horizontalLayout_2.addWidget(self.comboBoxPeriod)

        self.pushButtonReload = QPushButton(self.frame_2)
        self.pushButtonReload.setObjectName(u"pushButtonReload")

        self.horizontalLayout_2.addWidget(self.pushButtonReload)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidgetHistory = QTableWidget(self.frame_5)
        self.tableWidgetHistory.setObjectName(u"tableWidgetHistory")
        self.tableWidgetHistory.setMinimumSize(QSize(400, 0))
        self.tableWidgetHistory.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout_3.addWidget(self.tableWidgetHistory)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayoutPlotPrice = QVBoxLayout()
        self.verticalLayoutPlotPrice.setObjectName(u"verticalLayoutPlotPrice")

        self.verticalLayout_6.addLayout(self.verticalLayoutPlotPrice)

        self.verticalLayoutPlotAmout = QVBoxLayout()
        self.verticalLayoutPlotAmout.setObjectName(u"verticalLayoutPlotAmout")

        self.verticalLayout_6.addLayout(self.verticalLayoutPlotAmout)


        self.horizontalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1465, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.comboBoxMarket.setItemText(0, QCoreApplication.translate("MainWindow", u"KOSPI", None))
        self.comboBoxMarket.setItemText(1, QCoreApplication.translate("MainWindow", u"KOSDAQ", None))
        self.comboBoxMarket.setItemText(2, QCoreApplication.translate("MainWindow", u"NYSE", None))
        self.comboBoxMarket.setItemText(3, QCoreApplication.translate("MainWindow", u"NASDAQ", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.comboBoxPeriod.setItemText(0, QCoreApplication.translate("MainWindow", u"1 Year", None))
        self.comboBoxPeriod.setItemText(1, QCoreApplication.translate("MainWindow", u"6 Months", None))
        self.comboBoxPeriod.setItemText(2, QCoreApplication.translate("MainWindow", u"1 Month", None))
        self.comboBoxPeriod.setItemText(3, QCoreApplication.translate("MainWindow", u"2 Weeks", None))
        self.comboBoxPeriod.setItemText(4, QCoreApplication.translate("MainWindow", u"1 Week", None))
        self.comboBoxPeriod.setItemText(5, QCoreApplication.translate("MainWindow", u"Custom", None))

        self.pushButtonReload.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

