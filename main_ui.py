# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1302, 741)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
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
        self.tabWidget_2 = QTabWidget(self.frame)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setMinimumSize(QSize(250, 0))
        self.tabWidget_2.setMaximumSize(QSize(250, 16777215))
        self.tabAll = QWidget()
        self.tabAll.setObjectName(u"tabAll")
        self.verticalLayout_2 = QVBoxLayout(self.tabAll)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBoxMarket = QComboBox(self.tabAll)
        self.comboBoxMarket.addItem("")
        self.comboBoxMarket.addItem("")
        self.comboBoxMarket.addItem("")
        self.comboBoxMarket.addItem("")
        self.comboBoxMarket.setObjectName(u"comboBoxMarket")

        self.verticalLayout_2.addWidget(self.comboBoxMarket)

        self.listWidgetStocks = QListWidget(self.tabAll)
        self.listWidgetStocks.setObjectName(u"listWidgetStocks")

        self.verticalLayout_2.addWidget(self.listWidgetStocks)

        self.pushButtonAddSelected = QPushButton(self.tabAll)
        self.pushButtonAddSelected.setObjectName(u"pushButtonAddSelected")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonAddSelected.sizePolicy().hasHeightForWidth())
        self.pushButtonAddSelected.setSizePolicy(sizePolicy1)
        self.pushButtonAddSelected.setMinimumSize(QSize(0, 0))
        self.pushButtonAddSelected.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.pushButtonAddSelected)

        self.lineEditKeyWord = QLineEdit(self.tabAll)
        self.lineEditKeyWord.setObjectName(u"lineEditKeyWord")

        self.verticalLayout_2.addWidget(self.lineEditKeyWord)

        self.tabWidget_2.addTab(self.tabAll, "")
        self.tabSelected = QWidget()
        self.tabSelected.setObjectName(u"tabSelected")
        self.verticalLayout_5 = QVBoxLayout(self.tabSelected)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.listWidgetSelectedTickers = QListWidget(self.tabSelected)
        self.listWidgetSelectedTickers.setObjectName(u"listWidgetSelectedTickers")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidgetSelectedTickers.sizePolicy().hasHeightForWidth())
        self.listWidgetSelectedTickers.setSizePolicy(sizePolicy2)
        self.listWidgetSelectedTickers.setMinimumSize(QSize(0, 0))
        self.listWidgetSelectedTickers.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_5.addWidget(self.listWidgetSelectedTickers)

        self.pushButtonRemoveSelected = QPushButton(self.tabSelected)
        self.pushButtonRemoveSelected.setObjectName(u"pushButtonRemoveSelected")
        sizePolicy1.setHeightForWidth(self.pushButtonRemoveSelected.sizePolicy().hasHeightForWidth())
        self.pushButtonRemoveSelected.setSizePolicy(sizePolicy1)
        self.pushButtonRemoveSelected.setMinimumSize(QSize(0, 0))
        self.pushButtonRemoveSelected.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_5.addWidget(self.pushButtonRemoveSelected)

        self.tabWidget_2.addTab(self.tabSelected, "")

        self.horizontalLayout.addWidget(self.tabWidget_2)

        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabData = QWidget()
        self.tabData.setObjectName(u"tabData")
        self.verticalLayout_4 = QVBoxLayout(self.tabData)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.tabData)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.label)

        self.dateEditStart = QDateEdit(self.tabData)
        self.dateEditStart.setObjectName(u"dateEditStart")
        self.dateEditStart.setDateTime(QDateTime(QDate(2023, 12, 29), QTime(9, 0, 0)))

        self.horizontalLayout_2.addWidget(self.dateEditStart)

        self.label_2 = QLabel(self.tabData)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.dateEditEnd = QDateEdit(self.tabData)
        self.dateEditEnd.setObjectName(u"dateEditEnd")
        self.dateEditEnd.setDateTime(QDateTime(QDate(2024, 12, 29), QTime(9, 0, 0)))

        self.horizontalLayout_2.addWidget(self.dateEditEnd)

        self.comboBoxPeriod = QComboBox(self.tabData)
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.addItem("")
        self.comboBoxPeriod.setObjectName(u"comboBoxPeriod")

        self.horizontalLayout_2.addWidget(self.comboBoxPeriod)

        self.pushButtonReload = QPushButton(self.tabData)
        self.pushButtonReload.setObjectName(u"pushButtonReload")

        self.horizontalLayout_2.addWidget(self.pushButtonReload)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.frame_5 = QFrame(self.tabData)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy4)
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
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


        self.verticalLayout_4.addWidget(self.frame_5)

        self.tabWidget.addTab(self.tabData, "")
        self.tabTopDrops = QWidget()
        self.tabTopDrops.setObjectName(u"tabTopDrops")
        self.verticalLayout_3 = QVBoxLayout(self.tabTopDrops)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBoxDeclinersPeriod = QComboBox(self.tabTopDrops)
        self.comboBoxDeclinersPeriod.setObjectName(u"comboBoxDeclinersPeriod")

        self.horizontalLayout_4.addWidget(self.comboBoxDeclinersPeriod)

        self.pushButtonFindDecliners = QPushButton(self.tabTopDrops)
        self.pushButtonFindDecliners.setObjectName(u"pushButtonFindDecliners")

        self.horizontalLayout_4.addWidget(self.pushButtonFindDecliners)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidgetDecliners = QTableWidget(self.tabTopDrops)
        self.tableWidgetDecliners.setObjectName(u"tableWidgetDecliners")
        sizePolicy2.setHeightForWidth(self.tableWidgetDecliners.sizePolicy().hasHeightForWidth())
        self.tableWidgetDecliners.setSizePolicy(sizePolicy2)
        self.tableWidgetDecliners.setMinimumSize(QSize(350, 0))
        self.tableWidgetDecliners.setMaximumSize(QSize(350, 16777215))
        self.tableWidgetDecliners.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.horizontalLayout_5.addWidget(self.tableWidgetDecliners)

        self.webEngineViewNaver = QWebEngineView(self.tabTopDrops)
        self.webEngineViewNaver.setObjectName(u"webEngineViewNaver")
        self.webEngineViewNaver.setUrl(QUrl(u"https://finance.naver.com/"))

        self.horizontalLayout_5.addWidget(self.webEngineViewNaver)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tabTopDrops, "")
        self.tabTopDropsWeb = QWidget()
        self.tabTopDropsWeb.setObjectName(u"tabTopDropsWeb")
        self.verticalLayout_7 = QVBoxLayout(self.tabTopDropsWeb)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButtonDropWebBack = QPushButton(self.tabTopDropsWeb)
        self.pushButtonDropWebBack.setObjectName(u"pushButtonDropWebBack")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButtonDropWebBack.sizePolicy().hasHeightForWidth())
        self.pushButtonDropWebBack.setSizePolicy(sizePolicy5)
        self.pushButtonDropWebBack.setMinimumSize(QSize(50, 0))
        self.pushButtonDropWebBack.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_6.addWidget(self.pushButtonDropWebBack)

        self.pushButtonDropWebHome = QPushButton(self.tabTopDropsWeb)
        self.pushButtonDropWebHome.setObjectName(u"pushButtonDropWebHome")
        sizePolicy5.setHeightForWidth(self.pushButtonDropWebHome.sizePolicy().hasHeightForWidth())
        self.pushButtonDropWebHome.setSizePolicy(sizePolicy5)
        self.pushButtonDropWebHome.setMinimumSize(QSize(50, 0))
        self.pushButtonDropWebHome.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_6.addWidget(self.pushButtonDropWebHome)

        self.pushButtonDropWebForward = QPushButton(self.tabTopDropsWeb)
        self.pushButtonDropWebForward.setObjectName(u"pushButtonDropWebForward")
        sizePolicy5.setHeightForWidth(self.pushButtonDropWebForward.sizePolicy().hasHeightForWidth())
        self.pushButtonDropWebForward.setSizePolicy(sizePolicy5)
        self.pushButtonDropWebForward.setMinimumSize(QSize(50, 0))
        self.pushButtonDropWebForward.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_6.addWidget(self.pushButtonDropWebForward)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.webEngineViewKRX = QWebEngineView(self.tabTopDropsWeb)
        self.webEngineViewKRX.setObjectName(u"webEngineViewKRX")
        sizePolicy4.setHeightForWidth(self.webEngineViewKRX.sizePolicy().hasHeightForWidth())
        self.webEngineViewKRX.setSizePolicy(sizePolicy4)
        self.webEngineViewKRX.setUrl(QUrl(u"https://data.krx.co.kr/contents/MMC/RANK/rank/MMCRANK003.cmd"))

        self.verticalLayout_7.addWidget(self.webEngineViewKRX)

        self.tabWidget.addTab(self.tabTopDropsWeb, "")

        self.horizontalLayout.addWidget(self.tabWidget)


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
        self.menubar.setGeometry(QRect(0, 0, 1302, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.comboBoxMarket.setItemText(0, QCoreApplication.translate("MainWindow", u"KOSPI", None))
        self.comboBoxMarket.setItemText(1, QCoreApplication.translate("MainWindow", u"KOSDAQ", None))
        self.comboBoxMarket.setItemText(2, QCoreApplication.translate("MainWindow", u"NYSE", None))
        self.comboBoxMarket.setItemText(3, QCoreApplication.translate("MainWindow", u"NASDAQ", None))

        self.pushButtonAddSelected.setText(QCoreApplication.translate("MainWindow", u"Add to Selected", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabAll), QCoreApplication.translate("MainWindow", u"All", None))
        self.pushButtonRemoveSelected.setText(QCoreApplication.translate("MainWindow", u"Remove from Selected", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabSelected), QCoreApplication.translate("MainWindow", u"Selected", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.comboBoxPeriod.setItemText(0, QCoreApplication.translate("MainWindow", u"1 Year", None))
        self.comboBoxPeriod.setItemText(1, QCoreApplication.translate("MainWindow", u"6 Months", None))
        self.comboBoxPeriod.setItemText(2, QCoreApplication.translate("MainWindow", u"1 Month", None))
        self.comboBoxPeriod.setItemText(3, QCoreApplication.translate("MainWindow", u"2 Weeks", None))
        self.comboBoxPeriod.setItemText(4, QCoreApplication.translate("MainWindow", u"1 Week", None))
        self.comboBoxPeriod.setItemText(5, QCoreApplication.translate("MainWindow", u"Custom", None))

        self.pushButtonReload.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabData), QCoreApplication.translate("MainWindow", u"Data", None))
        self.pushButtonFindDecliners.setText(QCoreApplication.translate("MainWindow", u"Find Decliners", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTopDrops), QCoreApplication.translate("MainWindow", u"Top drops", None))
        self.pushButtonDropWebBack.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButtonDropWebHome.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.pushButtonDropWebForward.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTopDropsWeb), QCoreApplication.translate("MainWindow", u"Top Drops (web)", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

