from PyQt5 import QtWidgets
from untitled import Ui_MainWindow as  Aui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time

import sys


class work1(QThread):
    my_signal = pyqtSignal(int)
    my_signal2=pyqtSignal(int)
    def __init__(self):
        super(work1,self).__init__()
        self.count = 0
        self.is_on = True


    def run(self):
     for i in range(101):
          self.count = self.count+1
          self.my_signal2.emit(self.count)
          print(self.count)
          time.sleep(0.05)
          if self.count==50:
            self.is_on=False

class demo1(QtWidgets.QMainWindow,Aui):

    def __init__(self):
        super(demo1,self).__init__()
        self.setupUi(self)
        self.a = work1()
        self.a.my_signal2.connect(self.progress)

        self.a.my_signal.connect(self.progress)
    def slot1(self,i):
        self.a.is_on = True
        self.a.start()  # 启动线程

    def progress(self,i):
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(i)
        self.listWidget.addItem(str(i))
        return i




if __name__ == '__main__':
      app = QApplication(sys.argv)
      login = demo1()
      login.show()
      sys.exit(app.exec_())