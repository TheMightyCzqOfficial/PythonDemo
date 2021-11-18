from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from login import Ui_MainWindow as  Aui
from jisuanqiGUI import Calcu
from QT测试 import cs
from 一键爬虫界面 import pa
import time
import sys
class login1(QtWidgets.QMainWindow,Aui):


    def __init__(self):
        super(login1,self).__init__()
        self.setupUi(self)


    def login(self):


        user = self.lineEdit.text()
        pwd = self.lineEdit_2.text()

        if (user == "pachong" and pwd == ""):
            self.b = pa()
            self.b.show()
            self.close()
        if (user == "jisuanqi"and pwd==""):
            self.b =Calcu()
            self.b.show()
            self.close()
        elif(user == "amazon" and pwd == ""):
            self.b = cs()
            self.b.show()
            self.close()
        elif (user != "jsq"and user!="amazon"):
                self.label_4.setText("用户不存在")
        elif (pwd!=""):
            self.label_4.setText("用户存在,密码错误")

         #try:{
          # self.textEdit.setText(str(tester))}
       #  except:{
          # self.textEdit.setText("                           ERROR!!!                         ")}



if __name__ == '__main__':

      app = QApplication(sys.argv)
      login = login1()
      login.show()
      sys.exit(app.exec_())