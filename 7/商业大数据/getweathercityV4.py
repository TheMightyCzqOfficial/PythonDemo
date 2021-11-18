import sys  #系統用的lib
import requests #HTTP GET元件
import json     #解易json元件
import time     ##時間用的lib
import datetime #時間用的lib
from datetime import datetime       #轉unix time to date time 用的lib
import math     #數學用的lib
import os      #作業系統元件
import http.client  #網頁連線物件lib
import unicodedata  #解unicode用的lib
from pathlib import Path   #解路徑用的lib

from requests.exceptions import HTTPError       #連線錯誤的lib

import json
cnt = 0
# Opening JSON file
url = "INSERT INTO OW_citylist (MAC,sid, sname, country ,state ,lat, lon) VALUES ('Brucetsao','%s', '%s', '%s', '%s', '%s','%s')  ;\n"
f = open("citylist.sql", "w", encoding="utf-8")

with open('city.list.json',encoding='utf-8' ) as json_file:
    data = json.load(json_file)
# returns JSON object as

#data = json.load(f)

# Iterating through the json
# list
# Closing file
#f.close()
#print(data)
#table = json.loads(f)

    for table in data:
        s01 = table['id']
        s02 = table['name']
        s04 = table['state']
        s03 = table['country']
        s05 = table['coord']['lat']
        s06 = table['coord']['lon']
        s02a =s02
        s02a.replace("'","")
        s02a.replace("'","")
        s02a.replace("\"","")
        s02a.replace("'","")
        s02a.replace("'","")
        cnt = cnt+1
        print("NO:",cnt,s01,s02,"(",s02a,"/",s03,")",s04,s05,s06)
        #print(s01,s02,s03,s04,s05,s06,s07,s08,s09,s10,s11,s12,s13,s14,s15,s16)
        url1 = url % (s01,s02,s03,s04,s05,s06)
        url1.encode('utf8')
        print(url1)
        try:
            f.write(url1)
        except Exception as err:
            print('Other error occurred: {err}')
            sys.exit(0)
        else:
            print('Success!')
f.close()