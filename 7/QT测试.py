from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from amazonGUI import Ui_MainWindow
import sys
import test
import srww
import amazon

class cs(QtWidgets.QMainWindow,Ui_MainWindow):


    def __init__(self):
        super(cs,self).__init__()
        self.setupUi(self)
       # self.connection()

    def goback(self):
        from 登录页面 import login1
        self.a = login1()
        self.a.show()
        self.close()
    def setlabel(self):
        self.textEdit.selectAll()
        self.textEdit.copy()
        self.label_2.setText("已复制")

    def slot1(self):
        self.label_2.clear()
        self.textEdit.clear()
        text = self.lineEdit.text()
        #tester = test.test1(text)
        #tester = test.testlist()  #list
       # tester = test.testfor()
       # tester=jingdong.show(text)
        tester = amazon.geturl(text)
        print(text)
        if (text == "卢春勇"):
            self.textEdit.setText("8=========================D 卢春勇就是个鸡巴 8===========================D")
        elif (text == None):
                self.lineEdit.setText("请输入商品名！")
        elif (text == "黄显"):
            self.textEdit.setText("                          黄显巨鸡巴帅！")
        elif (text == "厉泽宇"):
            self.textEdit.setText("                             厉泽宇世界第一帅！")
        else:
            for i in tester:
                self.textEdit.insertPlainText(str(i))



if __name__ == '__main__':

      app = QApplication(sys.argv)
      ca = cs()
      ca.show()
      sys.exit(app.exec_())