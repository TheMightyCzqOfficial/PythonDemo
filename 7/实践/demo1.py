# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1078, 935)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 0, 621, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 0, 4);")
        self.label_3.setObjectName("label_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 80, 1081, 831))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(254, 222, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(530, 190, 31, 16))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(400, 190, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(220, 190, 121, 16))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 190, 81, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(330, 190, 71, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(590, 190, 131, 28))
        self.pushButton.setStyleSheet("background-color: rgb(192, 255, 251);")
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(380, 160, 161, 16))
        self.label_7.setObjectName("label_7")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab)
        self.listWidget_2.setGeometry(QtCore.QRect(180, 260, 541, 441))
        self.listWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(160, 230, 561, 20))
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.listWidget = QtWidgets.QListWidget(self.tab_3)
        self.listWidget.setGeometry(QtCore.QRect(240, 150, 481, 611))
        self.listWidget.setStyleSheet("background-color: rgb(226, 245, 255);")
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listWidget.setObjectName("listWidget")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 90, 93, 28))
        self.pushButton_5.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(420, 90, 93, 28))
        self.pushButton_6.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(310, 50, 101, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 50, 113, 21))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(240, 120, 561, 20))
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(550, 50, 271, 16))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 90, 121, 28))
        self.pushButton_3.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.browser2 = QtWebEngineWidgets.QWebEngineView(self.tab_2)
        self.browser2.setGeometry(QtCore.QRect(30, 50, 1041, 421))
        self.browser2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.browser2.setObjectName("browser2")
        self.browser1 = QtWebEngineWidgets.QWebEngineView(self.tab_2)
        self.browser1.setGeometry(QtCore.QRect(30, 470, 1041, 321))
        self.browser1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.browser1.setObjectName("browser1")
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_3.setGeometry(QtCore.QRect(30, 30, 931, 21))
        self.listWidget_3.setObjectName("listWidget_3")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(20, 10, 561, 20))
        self.label_11.setObjectName("label_11")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 20, 93, 28))
        self.pushButton_2.setStyleSheet("color: rgb(7, 7, 7);\n"
"background-color: rgb(240, 240, 240);")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget.currentChanged['int'].connect(MainWindow.change)
        self.pushButton.clicked.connect(MainWindow.slot1)
        self.pushButton_5.clicked.connect(MainWindow.add)
        self.pushButton_6.clicked.connect(MainWindow.delete)
        self.listWidget_2.doubleClicked['QModelIndex'].connect(MainWindow.addfrom1)
        self.pushButton_2.clicked.connect(MainWindow.shuoming)
        self.listWidget.itemClicked['QListWidgetItem*'].connect(MainWindow.selectstock)
        self.pushButton_3.clicked.connect(MainWindow.select)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "股票查询自选系统 v1.2"))
        self.label_4.setText(_translate("MainWindow", "支"))
        self.label_2.setText(_translate("MainWindow", "支 到"))
        self.label.setText(_translate("MainWindow", "输入查询的支数："))
        self.pushButton.setText(_translate("MainWindow", "查询所选股票"))
        self.label_7.setText(_translate("MainWindow", "区间最好<20(实时爬取)"))
        self.label_8.setText(_translate("MainWindow", "   代码    名字    地区    类型   年化收益 累计收益（2019至今） "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "股票查询界面"))
        self.pushButton_5.setText(_translate("MainWindow", "增加股票"))
        self.pushButton_6.setText(_translate("MainWindow", "删除股票"))
        self.label_5.setText(_translate("MainWindow", "输入股票代码："))
        self.label_6.setText(_translate("MainWindow", "   代码    名字    地区    类型   年化收益 累计收益（2019至今） "))
        self.pushButton_3.setText(_translate("MainWindow", "查看K线/柱状图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "股票自选池"))
        self.label_11.setText(_translate("MainWindow", "   代码    名字    地区    类型   年化收益 累计收益（2019至今） "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "K线/柱状图"))
        self.pushButton_2.setText(_translate("MainWindow", "操作说明"))
from PyQt5 import QtWebEngineWidgets
