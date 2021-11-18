from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from demo1 import Ui_MainWindow as  Aui
import sys
from demo2GUI import demo2

from get_stocks import get_final
class demo1(QtWidgets.QMainWindow,Aui):


    def __init__(self):
        super(demo1,self).__init__()
        self.setupUi(self)


    def slot1(self):
        start = self.lineEdit.text()
        end = self.lineEdit_2.text()
        data = get_final(eval(start),eval(end))
        self.textEdit.setText(str(data))
    def page2(self):
        self.a= demo2()
        self.a.show()













if __name__ == '__main__':

      app = QApplication(sys.argv)
      login = demo1()
      login.show()
      sys.exit(app.exec_())