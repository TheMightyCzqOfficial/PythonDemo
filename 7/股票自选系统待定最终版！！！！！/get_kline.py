import tushare as ts
import pandas as pd
import os
from  get_earning import  get_name
from pyecharts import Kline
def kline(get_stockcode):
    str_stockcode = str(get_stockcode)
    str_stockcode = str_stockcode.strip()  # 删除前后空格字符
    if 6 > len(str_stockcode) > 0:
        str_stockcode = str_stockcode.zfill(6) + '.SZ'  # zfill()函数返回指定长度的字符串，原字符串右对齐，前面填充0
    if len(str_stockcode) == 6:
        if str_stockcode[0:1] == '0':
            str_stockcode = str_stockcode + '.SZ'
        if str_stockcode[0:1] == '3':
            str_stockcode = str_stockcode + '.SZ'
        if str_stockcode[0:1] == '6':
            str_stockcode = str_stockcode + '.SH'
    pro = ts.pro_api('0c83b5844e98bd675c51f58027f21e6f6547e836d364ec09f5e0ff3f')
    df = pro.daily(ts_code=str_stockcode, start_date='20180101', end_date='')
    v3=list(df.loc[:,['open','close','low','high']].values)
    v2=list(pd.to_datetime(df.trade_date, format='%Y%m%d'))
    v1=v3[::-1]
    v0=v2[::-1]
    name = get_name(get_stockcode)
    kline = Kline(name+"K线图",title_text_size=15)
    kline.add("", v0, v1,is_datazoom_show=True,
            mark_line=["average"],
            mark_point=["max", "min"],
            mark_point_symbolsize=60,
            mark_line_valuedim=['highest', 'lowest'] )
    kline.render('./html/K线.html')

if __name__=='__main__':
 kline(input())