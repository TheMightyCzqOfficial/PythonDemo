import tushare as ts
from sqlalchemy import create_engine
from pyfinance import TSeries
import pandas as pd
import os

import numpy as np
def panduan_stock(code):
    df = ts.get_k_data(code, '', '')
    if str(df) == "Empty DataFrame\nColumns: []\nIndex: []":
        print("123")
        return 5
    else:
        return 1
def get_data(code):
        pro = ts.pro_api('d270e0a0d72208d1ce188b8893f1d477ef84d76efc4e6a88a47e992d')
        #df = pro.daily(ts_code=code, start_date='20180701', end_date='')
        df = ts.get_k_data(code, '', '')
        if str(df)=="Empty DataFrame\nColumns: []\nIndex: []":
            print("123")
            return 5
        else:
            df.index = pd.to_datetime(df.date)
            ret = df.close / df.close.shift(1) - 1
            #print(ret)
            return (TSeries(ret.dropna()))

def progressbar():
    item = 0
    a = item +1
    print(a)
    return a

def get_shouyi(start,end):
    from get_stocks import get_all
    code = get_all(start,end)
    list = []
    list1 = []
    item = 0
    for i in code.symbol:
        progressbar()
        tss = get_data(i)
        anl_ret = tss.anlzd_ret()
        # 累计收益率
        cum_ret = tss.cuml_ret()
        # 计算周期收益率
        q_ret = tss.rollup('Q')
        a_ret = tss.rollup('A')
        #print(f'年化收益率：{anl_ret * 100:.2f}%')
        #print(f'累计收益率：{cum_ret * 100:.2f}%')
        an = ('%.2f'%(anl_ret*100)+"%")#年化收益率
        cu = ('%.2f'%(cum_ret*100)+"%")#累计收益率
        #print(an)
        #print(cu)
        list.append(an)
        list1.append(cu)
        item=item+1
    code['年化收益率     '] = list
    code['累计收益率（2019至今）'] = list1
    data = code.values.tolist()
    print(str(data))
    return (data)

def get_shouyiByNo(get_stockcode):
        list = []
        list1 = []
        tss = get_data(get_stockcode)
        anl_ret = tss.anlzd_ret()
        # 累计收益率
        cum_ret = tss.cuml_ret()
        # 计算周期收益率
        q_ret = tss.rollup('Q')
        a_ret = tss.rollup('A')
        #print(f'年化收益率：{anl_ret * 100:.2f}%')
        #print(f'累计收益率：{cum_ret * 100:.2f}%')
        an = ('%.2f'%(anl_ret*100)+"%")#年化收益率
        cu = ('%.2f'%(cum_ret*100)+"%")#累计收益率
        #print(an)
        #print(cu)
        list.append(an)
        list1.append(cu)
        return (list,list1)



def get_name(code):
    '''通过股票代码导出公司名称'''

    pro = ts.pro_api('d270e0a0d72208d1ce188b8893f1d477ef84d76efc4e6a88a47e992d')

    dat = pro.query('stock_basic', fields='symbol,name')

    company_name = list(dat.loc[dat['symbol'] == code].name)[0]
    print(company_name)
    return company_name

def open():
    os.system("render.html")
def gif(code):
    tss = get_data(code)
    name=get_name(code)
    q_ret = tss.rollup('Q')
    from pyecharts import Bar
    attr = q_ret.index.strftime('%Y%m')
    v1 = (q_ret * 100).round(2).values
    bar = Bar(name+'收益率%')
    bar.add('', attr, v1, )
    bar.render('./html/柱状图.html')

if __name__ == "__main__":
    code = input()
    #get_name(str(code))
   # get_shouyi()
    #gif(str(code))
    #open()
    get_data(code)

