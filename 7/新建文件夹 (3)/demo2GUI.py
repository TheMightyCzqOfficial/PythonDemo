from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from demo2 import Ui_MainWindow as  Aui
import sys
from connect_database import selectall,delete,add
from get_stocks import getByNo


from get_stocks import get_final
class demo2(QtWidgets.QMainWindow,Aui):


    def __init__(self):
        super(demo2,self).__init__()
        self.setupUi(self)


    def all(self):
        self.textEdit.clear()
        all = selectall()
        text = getByNo(all)
        #print(text)
        self.textEdit.insertPlainText(str(text))



    def delete(self):
        text = self.lineEdit.text()
        delete(text)
        self.all()
    def add(self):
        text = self.lineEdit.text()
        add(text)
        self.all()
    def goback(self):
        from StockSelecter_mainwindow import demo1
        self.a = demo1()
        self.a.show()
        self.close()










if __name__ == '__main__':

      app = QApplication(sys.argv)
      login = demo2()
      login.show()
      sys.exit(app.exec_())