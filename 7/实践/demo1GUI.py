from PyQt5 import QtWidgets,QtCore
from demo1 import Ui_MainWindow as  Aui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys
import  time
from connect_database import addstock,selectstock,deletestock,select_one
from get_earning import get_shouyi



class demo1(QtWidgets.QMainWindow,Aui):


    def __init__(self):
        super(demo1,self).__init__()
        self.setupUi(self)



    def slot1(self):
        QApplication.processEvents()
        self.listWidget_2.clear()
        start = self.lineEdit.text()
        end = self.lineEdit_2.text()
        # print(eval(start+"-1"))
        if start == "" or end == "":
            res_1 = QMessageBox.information(self, "标题", "输入错误请检查！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        elif eval(start) > eval(end) or start == "0":
            res_1 = QMessageBox.information(self, "标题", "输入错误请检查！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        else:

            data = get_shouyi(eval(start + "-1"), eval(end))
            for i in data:
                QApplication.processEvents()
                time.sleep(0.02)
                self.listWidget_2.addItem(str(i))

    def all(self):
        self.listWidget.clear()
        all = selectstock()
        #print(text)
        for i in all:
            QApplication.processEvents()
            time.sleep(0.0256789)
            self.listWidget.addItem(str(i))
    def delete(self):
        from get_earning import get_name
        text = self.lineEdit_3.text()
        name = get_name(text)
        if text=="":
            res_1 = QMessageBox.information(self, "标题","未读取到股票数据，请选择或输入！", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)

        else:
            deletestock(text)
        self.all()
        self.label_10.setText("删除的股票为"+text+" "+name+"注意保留！！！")
        res_2 = QMessageBox.information(self, "标题", "删除成功！", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)


    def add(self):
        from get_earning import get_name
        text = self.lineEdit_3.text()
        name = get_name(text)
        if text=="":
            res_1 = QMessageBox.information(self, "标题", "股票代码输入错误,请检查！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        else:
            addstock(text)
            res_1 = QMessageBox.information(self, "标题", "添加股票"+text+" "+name+"成功！", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        self.lineEdit_3.clear()
        self.label_10.clear()

        self.all()
    def addfrom1(self):
        import re
        from  get_earning import get_name
        a = self.listWidget_2.selectedItems()
        text = [i.text() for i in list(a)]
        b = re.findall("\d{6}", str(text))
        addstock(b[0])
        name = get_name(b[0])
        res_1 = QMessageBox.information(self, "添加提示", ""+b[0]+" "+name+"已成功添加到自选池，请前往查看！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def change(self):
        a = self.tabWidget.currentIndex()
        if self.tabWidget.currentIndex() == 1:
            self.all()
    def shuoming(self):
        res_1 = QMessageBox.information(self, "操作说明"," 双击股票添加到自选池"+"\n"+"股票自选池单击选中进行操作",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


    def select(self):
        from get_earning import gif,get_name
        from get_kline import kline
        #print(b[0])
        a = self.lineEdit_3.text()
        if a=="":
            res_1 = QMessageBox.information(self, "标题", "未选择股票,请检查！", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            gif(a)
            kline(a)
            name = get_name(a)
            data = select_one(a)

            self.browser1.load(QUrl(QFileInfo("./html/柱状图.html").absoluteFilePath()))
            self.browser2.load(QUrl(QFileInfo("./html/K线.html").absoluteFilePath()))
            self.listWidget_3.clear()
            self.listWidget_3.addItem(str(data))
            self.tabWidget.setCurrentIndex(2)

       # self.listWidget.
    def selectstock(self):
        import re
        from get_earning import  get_name
        a = self.listWidget.selectedItems()
        text = [i.text() for i in list(a)]
        b = re.findall("\d{6}", str(text))
        name = get_name(b[0])
        res_1 = QMessageBox.information(self, "操作说明", "已选中 "+name+"",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        print(res_1)
        self.label_10.setText("当前已选中 "+name)
        self.lineEdit_3.setText(b[0])



    def close(self):
        self.close()










if __name__ == '__main__':

      app = QApplication(sys.argv)
      login = demo1()
      login.show()
      sys.exit(app.exec_())