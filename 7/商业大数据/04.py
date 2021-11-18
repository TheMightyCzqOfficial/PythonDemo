import sys  #系統用的lib
import requests #HTTP GET元件
import json     #解易json元件
import time     ##時間用的lib
import datetime #時間用的lib
import math     #數學用的lib
import os      #作業系統元件
import http.client  #網頁連線物件lib
import unicodedata  #解unicode用的lib
from pathlib import Path   #解路徑用的lib

from requests.exceptions import HTTPError       #連線錯誤的lib
def getweather(name):
    url = 'https://samples.openweathermap.org/data/2.5/weather?q='+str(name)+',cn&appid=b6907d289e10d714a6e88b30761fae22'
    ##需要城市修改q之后的城市名称即可
    ##url='https://samples.openweathermap.org/data/2.5/weather?q=Beijing,cn,cn&appid=b6907d289e10d714a6e88b30761fae22'
    try:
        res = requests.get(url)
        res.raise_for_status()
    except HTTPError as http_err:
        print('HTTP error occurred: {http_err}')
        sys.exit(0)
    except Exception as err:
        print('Other error occurred: {err}')
        sys.exit(0)
    else:
        print('Success!')
        table = json.loads(res.content.decode('utf-8'))

    s01 = table['coord']['lon']
    s02 = table['coord']['lat']
    s03 = table['main']['temp']
    s04 = table['main']['humidity']

    print("地理位置是：", s01, s02)
    print("温度是：", s03)
    print("湿度百分比是：", s04)