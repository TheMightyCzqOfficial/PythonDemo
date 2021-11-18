import tushare as ts
from pyfinance import TSeries
import numpy as np
import  os
import pandas as pd


def get_data(code, start='2011-01-01', end=''):
    df = ts.get_k_data(code, start, end)
    df.index = pd.to_datetime(df.date)
    ret = df.close / df.close.shift(1) - 1
    return TSeries(ret.dropna())
def run(code):
    tss = get_data('601318')
    anl_ret = tss.anlzd_ret()
    # 累计收益率
    cum_ret = tss.cuml_ret()
    # 计算周期收益率
    q_ret = tss.rollup('Q')
    a_ret = tss.rollup('A')


    print(f'年化收益率：{anl_ret * 100:.2f}%')
    print(f'累计收益率：{cum_ret * 100:.2f}%')

    from pyecharts import Bar
    attr=q_ret.index.strftime('%Y%m')
    v1=(q_ret*100).round(2).values
    bar=Bar('中国平安各季度收益率%')
    bar.add('',attr,v1,)
    bar.render()
os.system("render.html")