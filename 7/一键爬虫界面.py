from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from yijianpachong import Ui_MainWindow
import sys
import requests
from bs4 import BeautifulSoup
from 一键爬虫代码 import origin
from 一键爬虫代码 import run


class pa(QtWidgets.QMainWindow,Ui_MainWindow):


    def __init__(self):
        super(pa,self).__init__()
        self.setupUi(self)
    def goback(self):
        from 登录页面 import login1
        self.a = login1()
        self.a.show()
        self.close()
    def run(self):
     self.textEdit.clear()
     res = origin(self.lineEdit.text())
     try:{
         self.textEdit.insertPlainText(res)
          }
     except:{self.textEdit.setText("error")}

    def slot1(self):
        self.textEdit.clear()
        text=self.lineEdit_3.text()
        result = run(self.lineEdit.text(),text)
        try:
            {
                self.textEdit.insertPlainText(str(result))
            }
        except:
            {self.textEdit.setText("error")}




if __name__ == '__main__':

      app = QApplication(sys.argv)
      ca = pa()
      ca.show()
      sys.exit(app.exec_())