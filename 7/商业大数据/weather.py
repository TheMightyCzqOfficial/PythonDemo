import requests
import re
import pymysql
import  time
import numpy as np
import pandas as pd
def getweather():
    header = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400"
        ,"Cookie":"_ga=GA1.2.696185697.1620615102; _gid=GA1.2.604994329.1620615102; __gads=ID=19b1095366056791-220c3c68f2c700a2:T=1620615103:RT=1620615103:S=ALNI_MYlyVJXijpu0AF0cZh3SwLAIihjoA; signed_in=czq624"
    }
    data={}
    tem_list=[]
    hum_list=[]
    data_list = []
    city=["Nanping","Changde","Putian","Zhangzhou","Quanzhou","Sanming","Shaowu","Wuhu","Yancheng","Fuzhou"
        ,"Chongqing","Foshan","Huludao","Changsha","Guizhou","Shijiazhuang","Baoding","Qingdao","Tangshan","Handan"
          ,"Sanya","Cangzhou","Hengshui","Haikou","Jinan","Zibo","Weifang","Nanjing","Shunde","Jinzhou"]
    for i in city:

        url="https://api.openweathermap.org/data/2.5/weather?q="+i+"&appid=b0c21681ec5364b76facc9115f45d0dc"
        res=requests.get(url,headers=header)
        content = res.content.decode(res.apparent_encoding)
        print(content)
        name=i
        tem=re.findall("\"feels_like\":(.*?),",content)
        humi=re.findall("\"humidity\":(.*?),",content)
        sheshidu=eval(tem[0]+"-272.15")
        wendu=int(sheshidu)
        print(int(sheshidu))
        data_list.append(name)
       # data.append(int(sheshidu))
        #data.append(humi[0]+"%")
        tem_list.append(str(wendu))
        hum_list.append(humi[0]+"%")
        print(data_list)
        print(tem_list)
        print(hum_list)
        #addinto(data)
        #select()
        dic1 = {'名字': data_list,
                '温度': tem_list, '湿度': hum_list}  # 使用字典进行输入
        test_3 = pd.DataFrame(dic1)
        print(test_3)
        time.sleep(1)
    dic1 = {'名字': data_list,
            '温度':tem_list, '湿度':hum_list}  # 使用字典进行输入
    test_3 = pd.DataFrame(dic1)
    print(test_3)
def addinto(code):

    conn = pymysql.connect(host='localhost', port=3306, user="root", passwd="chen2000624.", db="weather",
                           charset="utf8")
    cursor = conn.cursor()
    add = "insert ignore into data values('"+str(code[0])+"','"+str(code[1])+"','"+str(code[2])+"')"

    try:
        {
                cursor.execute(add),
                print("添加天气信息成功！")
        }
    except:
            {
                print("添加错误！")
            }

    conn.commit()
    cursor.close()
    conn.close()
def select():
    conn = pymysql.connect(host='localhost', port=3306, user="root", passwd="chen2000624.", db="weather",
                           charset="utf8")
    cursor = conn.cursor()
    select = "select * from data order by name desc"
    try:
        {
            cursor.execute(select)
        }
    except:
        {
            print("查询错误！")
        }
    last_id = cursor.fetchall()

    print("天气信息:")
    for i in last_id:
        print(i)
    return last_id
    cursor.close()
    conn.close()
if __name__=="__main__":
    select()
    #getweather()

