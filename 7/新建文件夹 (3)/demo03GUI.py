import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from demo03 import Ui_MainWindow

from get_earning import get_name, gif


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
    def getgif(self):
        code = self.lineEdit.text()
        name=get_name(code)
        gif(code)
        self.setWindowTitle(name + '柱状图')  # 窗口标题
        self.setGeometry(400,400, 888, 450)  # 窗口的大小和位置设置
        self.browser = QWebEngineView()
        # 加载外部的web界面
        self.browser.load(QUrl(QFileInfo("./"+name+".html").absoluteFilePath()))
        self.setCentralWidget(self.browser)
    def slot1(self):
     self.listView.deleteLater()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec_())