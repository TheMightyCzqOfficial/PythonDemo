import tushare as ts
import pandas as pd
from get_earning import  get_shouyi
def get_all(start,end):
    from get_earning import get_shouyi
    pro = ts.pro_api('0c83b5844e98bd675c51f58027f21e6f6547e836d364ec09f5e0ff3f')
    data = pro.query('stock_basic', exchange='', list_status='L', fields='symbol,name,area,industry')
    n10 = data[start:end]
    return n10


def insert(get_stockcode):
        from get_earning import get_shouyiByNo
        list2 = []
        print(get_shouyiByNo(get_stockcode))
        list, list1 = get_shouyiByNo(get_stockcode)
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
        data = pro.stock_basic(ts_code=str_stockcode, exchange='', list_status='L', fields='symbol,name,area,industry')
        data.rename(columns={"symbol": "", "name": "", "area": "", "industry": ""}, inplace=True)
        n11 = pd.DataFrame(data)
        n11['abc'] = list
        n11['cde'] = list1
        a=n11.values.tolist()
        list2=list2+a
        print(list2)
        return list2
def getByNo(get_stockcode): # 输入的数字股票代码转换成字符串股票代码
    from get_earning import get_shouyiByNo
    a=pd.DataFrame(data=None,columns={})
    list2 = []
    for i in get_stockcode:
      list,list1 = get_shouyiByNo(i)
      str_stockcode = str(i)
      str_stockcode = str_stockcode.strip() # 删除前后空格字符
      if 6 > len(str_stockcode) > 0:
        str_stockcode = str_stockcode.zfill(6) + '.SZ' # zfill()函数返回指定长度的字符串，原字符串右对齐，前面填充0
      if len(str_stockcode) == 6:
        if str_stockcode[0:1] == '0':
          str_stockcode = str_stockcode + '.SZ'
        if str_stockcode[0:1] == '3':
          str_stockcode = str_stockcode + '.SZ'
        if str_stockcode[0:1] == '6':
          str_stockcode = str_stockcode + '.SH'
      pro = ts.pro_api('0c83b5844e98bd675c51f58027f21e6f6547e836d364ec09f5e0ff3f')
      data = pro.stock_basic(ts_code = str_stockcode, exchange='', list_status='L', fields='symbol,name,area,industry')
      data.rename(columns={"symbol": "", "name": "", "area": "", "industry": ""}, inplace=True)
      n11 = pd.DataFrame(data)
      n11['abc'] = list
      n11['cde'] = list1
      a=a.append(n11.values.tolist(),ignore_index=True)

    #a.rename(columns={"1": "股票代码", "2": "股票名称", "3": "地区", "4": "类型","5":"年化收益率  累计收益率          "},inplace=True)
    b=pd.DataFrame(a)
    b.columns=["股票代码","股票名称","地区","类型","年化收益率   ","累计收益率(2019至今)"]
    print(b)
    return b





if __name__ == "__main__":
    #a=eval(input("start"))
    #b=eval(input("end"))
    #get_shouyi(a,b)
    #selectall = selectall()
    #getByNo(selectall)
    insert(input())