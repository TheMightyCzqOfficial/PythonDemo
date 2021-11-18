from PyQt5 import QtWidgets
from demo1 import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from pyfinance import TSeries
import pandas as pd
import  tushare as ts
import  time
from connect_database import addstock,selectstock,deletestock,select_one

global start,end


class work1(QThread):
    my_signal = pyqtSignal(list)
    my_signal2 = pyqtSignal(int)
    def __init__(self):
        super(work1,self).__init__()

        self.is_on = True

    def get_all(self,start, end):
        print("get_all")
        print(start)
        pro = ts.pro_api('0c83b5844e98bd675c51f58027f21e6f6547e836d364ec09f5e0ff3f')
        data = pro.query('stock_basic', exchange='', list_status='L', fields='symbol,name,area,industry')
        n10 = data[int(start):int(end)]
        print("get_all end")
        return n10

    def get_data(self,code):
        print("get_data")
        print(start)
        #pro = ts.pro_api('d270e0a0d72208d1ce188b8893f1d477ef84d76efc4e6a88a47e992d')
        # df = pro.daily(ts_code=code, start_date='20180701', end_date='')
        df = ts.get_k_data(code, '', '')
        if str(df) == "Empty DataFrame\nColumns: []\nIndex: []":
            print("123")
            return 1
        else:
            df.index = pd.to_datetime(df.date)
            ret = df.close / df.close.shift(1) - 1
            return TSeries(ret.dropna())
    def get_shouyi(self,start, end):
        print("get_shouyi")
        print(start)
        code = self.get_all(start, end)
        list = []
        list1 = []
        self.count = 1
        for i in code.symbol:
            self.my_signal2.emit(self.count)
            tss = self.get_data(i)
            anl_ret = tss.anlzd_ret()
            # 累计收益率
            cum_ret = tss.cuml_ret()
            # 计算周期收益率
            q_ret = tss.rollup('Q')
            a_ret = tss.rollup('A')
            # print(f'年化收益率：{anl_ret * 100:.2f}%')
            # print(f'累计收益率：{cum_ret * 100:.2f}%')
            an = ('%.2f' % (anl_ret * 100) + "%")  # 年化收益率
            cu = ('%.2f' % (cum_ret * 100) + "%")  # 累计收益率
            # print(an)
            # print(cu)
            list.append(an)
            list1.append(cu)
            self.count=self.count+1
        code['年化收益率     '] = list
        code['累计收益率（2019至今）'] = list1
        data = code.values.tolist()
        print(str(data))
        return (data)

    def run(self):
        global  start,end
        print("线程启动")
        print(start+end)
    # while self.is_on:
          #self.count = self.count+1
        #Stock.progress(self)
        haha = self.get_shouyi(start, end)
        self.my_signal.emit(haha)
          #print(self.count)
          #time.sleep(0.5)



class Stock(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Stock,self).__init__()
        self.setupUi(self)
        self.a = work1()
        self.a.my_signal.connect(self.progress)
        self.a.my_signal2.connect(self.bar)
        self.progressBar.hide()


    def bar(self,i):
        print(i)
        self.progressBar.setValue(i)
        if i==eval(end + "-" + start):
            self.progressBar.hide()
    def progress(self,signal):
        print("12345")
        self.listWidget_2.clear()
        s = self.lineEdit.text()
        e = self.lineEdit_2.text()
        pro = eval(e +"-"+ s)
        print(pro)
        self.progressBar.setMaximum(pro)
        # print(eval(start+"-1"))
        if s == "" or e == "":
            QMessageBox.information(self, "标题", "输入错误请检查！", QMessageBox.Yes, QMessageBox.Yes)

        elif eval(s) > eval(e) or start == "0":
            QMessageBox.information(self, "标题", "输入错误请检查！", QMessageBox.Yes, QMessageBox.Yes)

        else:

            data = signal#Stock.get_shouyi(eval(start + "-1"), eval(end))
            #self.progressBar.setValue(b)
            if str(data) == "[]":
                QMessageBox.information(self, "标题", "范围内没有股票信息！", QMessageBox.Yes, QMessageBox.Yes)

            for item in data:
                QApplication.processEvents()
                self.listWidget_2.addItem(str(item) + "\n")




    def slot1(self,i):
        global start, end
        start = self.lineEdit.text()
        end = self.lineEdit_2.text()
        if start == "" or end == "":
            QMessageBox.information(self, "标题", "输入错误请检查！", QMessageBox.Yes, QMessageBox.Yes)

        elif eval(end + "-" + start) <0:
            QMessageBox.information(self, "标题", "输入错误请检查！", QMessageBox.Yes, QMessageBox.Yes)

        else:
            if self.progressBar.isHidden():
                self.progressBar.show()
            self.listWidget_2.clear()
            self.progressBar.reset()
            a = eval(end + "-" + start)
            self.progressBar.setMaximum(a)
            self.a.start()  # 启动线程



    def all(self):
        self.listWidget.clear()
        all = selectstock()
        #print(text)
        for i in all:
            QApplication.processEvents()
            time.sleep(0.015)
            self.listWidget.addItem(str(i)+"\n")
    def delete(self):
        from get_earning import get_name
        text = self.lineEdit_3.text()
        if text=="":
            QMessageBox.information(self, "标题", "未读取到股票数据，请选择或输入！", QMessageBox.Yes, QMessageBox.Yes)
        else:
          a=select_one(text)
            #print(str(a))
          if str(a)=="()":
             QMessageBox.information(self, "标题", "未读取到股票数据，请选择或输入！", QMessageBox.Yes, QMessageBox.Yes)
          else:
            name = get_name(text)
            deletestock(text)
            QMessageBox.information(self, "标题", "删除成功！", QMessageBox.Yes , QMessageBox.Yes)
            self.label_10.setText("删除的股票为" + text + " " + name + "注意保留！！！")
        self.all()




    def add(self):
        from get_earning import get_name,panduan_stock
        text = self.lineEdit_3.text()
        if text=="":
             QMessageBox.information(self, "标题", "股票代码输入错误,请检查！", QMessageBox.Yes, QMessageBox.Yes)
        else:
            print(text)
            a=select_one(text)
            b=panduan_stock(text)
            print(str(type(b)))
            print(1)
            if str(a)!="()":
                 QMessageBox.information(self, "标题", "股票已存在！", QMessageBox.Yes, QMessageBox.Yes)
            #
            elif b==5:
                    QMessageBox.information(self, "标题", "股票不存在！", QMessageBox.Yes, QMessageBox.Yes)
            elif b==1:
                name = get_name(text)
                print(name)
                addstock(text)
                QMessageBox.information(self, "标题", "添加股票" + text + " " + name + "成功！", QMessageBox.Yes,QMessageBox.Yes)
            self.lineEdit_3.clear()
            self.label_10.clear()
            self.all()
    def addfrom1(self):
        import re
        from  get_earning import get_name
        a = self.listWidget_2.selectedItems()
        text = [i.text() for i in list(a)]
        b = re.findall("\d{6}", str(text))
        for i in b:
            d=i
        c = select_one(eval(d))
        if str(c)!="()":
            QMessageBox.information(self, "标题", "股票已存在！", QMessageBox.Yes, QMessageBox.Yes)
        else:
            b = re.findall("\d{6}", str(text))
            addstock(b[0])
            name = get_name(b[0])
            QMessageBox.information(self, "添加提示", ""+b[0]+" "+name+"已成功添加到自选池，请前往查看！", QMessageBox.Yes, QMessageBox.Yes)

    def change(self):
        a = self.tabWidget.currentIndex()
        if self.tabWidget.currentIndex() == 1:
            self.all()
    def shuoming(self):
        QMessageBox.information(self, "操作说明"," 双击股票添加到自选池"+"\n"+"股票自选池单击选中进行操作"+"\n"+"实时获取股票数据，查询范围最好小于20",QMessageBox.Yes , QMessageBox.Yes)


    def select(self):
        from get_earning import gif,get_name,panduan_stock
        from get_kline import kline
        #print(b[0])
        a = self.lineEdit_3.text()
        b = panduan_stock(a)
        if a=="":
            QMessageBox.information(self, "标题", "未选择股票,请检查！", QMessageBox.Yes,QMessageBox.Yes)
        elif b==5:
            QMessageBox.information(self, "标题", "股票不存在！", QMessageBox.Yes, QMessageBox.Yes)
        else:
            gif(a)
            kline(a)
            name = get_name(a)
            data = select_one(a)
            self.browser1.load(QUrl(QFileInfo("./html/柱状图.html").absoluteFilePath()))
            self.browser2.load(QUrl(QFileInfo("./html/K线.html").absoluteFilePath()))
            self.listWidget_3.clear()
            for i in data:
             self.listWidget_3.addItem(str(i))
            self.tabWidget.setCurrentIndex(2)

       # self.listWidget.
    def selectstock(self):
        import re
        from get_earning import  get_name
        a = self.listWidget.selectedItems()
        text = [i.text() for i in list(a)]
        b = re.findall("\d{6}", str(text))
        name = get_name(b[0])
        QMessageBox.information(self, "操作说明", "已选中 "+name+"",QMessageBox.Yes, QMessageBox.Yes)
        self.label_10.setText("当前已选中 "+name)
        self.lineEdit_3.setText(b[0])




if __name__ == '__main__':

      app = QApplication(sys.argv)
      a=Stock()
      a.show()
      sys.exit(app.exec_())