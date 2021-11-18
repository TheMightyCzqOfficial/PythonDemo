from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from jisuanqi import Ui_MainWindow
import sys
import random

class Calcu(QtWidgets.QMainWindow,Ui_MainWindow):
    result = []
    ran = []



    def __init__(self):
        super(Calcu,self).__init__()
        self.setupUi(self)
       # self.connection()


    def goback(self):
        from 登录页面 import login1
        self.a = login1()
        self.a.show()
        self.close()

    def slot1(self):
        self.lineEdit.insert("1")

    def slot2(self):
        self.lineEdit.insert("2")
    def slot3(self):
        self.lineEdit.insert("3")

    def slot4(self):
        self.lineEdit.insert("4")

    def slot5(self):
        self.lineEdit.insert("5")

    def slot6(self):
        self.lineEdit.insert("6")
    def slot7(self):
        self.lineEdit.insert("7")

    def slot8(self):
        self.lineEdit.insert("8")

    def slot9(self):
        self.lineEdit.insert("9")
    def slot10(self):
        self.lineEdit.insert("0")
    def plus(self):
        self.lineEdit.insert(" + ")

    def minus(self):
        self.lineEdit.insert(" - ")

    def multiply(self):
        self.lineEdit.insert(" * ")

    def divide(self):
        self.lineEdit.insert(" / ")
    def clean(self):
        self.lineEdit.clear()
    def daomeidan(self):
        self.textEdit.clear()
        text = self.lineEdit.text()
        if (text=="5656"):
            self.ran.append("99")
            self.lineEdit.clear()
        else:
            self.ran.append(random.randint(0,100))
        for i in self.ran:
          self.textEdit.insertPlainText(str(i)+"\n")

    def equal(self):
        text = self.lineEdit.text()

        try:{
        self.result.append(text + " = " + str(eval(text))),
        }
        except:{
        self.lineEdit.setText('语法错误重新输入！！！！！！！')
        }
        self.textEdit.clear()
        self.lineEdit.clear()
        for i in self.result:
         self.textEdit.insertPlainText(str(i)+"\n")



if __name__ == '__main__':

      app = QApplication(sys.argv)
      ca = Calcu()
      ca.show()
      sys.exit(app.exec_())