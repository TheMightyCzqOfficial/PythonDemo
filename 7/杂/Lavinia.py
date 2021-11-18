import requests
import re
import base64
from io import BytesIO
import time
import os
def index():
    header = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }

    url0 = "https://www.uu131.net/plus/search.php?keyword=Lavinia%C8%E2%C8%E2&PageNo=3"
    res = requests.get(url0,headers=header, verify=False)
    content=re.findall("\"(.*?)\"  target=\"_blank\" class=\"dl-pic",res.text)
    num=1
    for i in content:
        url=i
        res1 = requests.get(url, headers=header, verify=False)
        content1 = res1.content.decode(res.apparent_encoding)
        result = re.findall("共(.*?)页", content1)
        page = int(result[0])
        s = i.replace(".html", "")
        for next in range(page-1):
            u = s + "_" + str(next + 1) + ".html"
            if(next==0):
                urls=re.findall("<img src=\"(.*?)\" alt=", content1)
                for p in urls:
                    r = requests.get(p, headers=header)
                    ls_f = base64.b64encode(BytesIO(r.content).read())
                    imgdata = base64.b64decode(ls_f)
                    name = "D:\\Lavinian\\" + str(num) + ".jpg"
                    with open(name, 'wb') as f:
                        f.write(imgdata)
                    print(str(num) + "下载成功")
                    #time.sleep(1)
                    num += 1
            else:
                resn = requests.get(u, headers=header, verify=False)
                contentn = resn.content.decode(res.apparent_encoding)
                urln = re.findall("<img src=\"(.*?)\" alt=", contentn)
                for p in urln:
                    r = requests.get(p, headers=header)
                    ls_f = base64.b64encode(BytesIO(r.content).read())
                    imgdata = base64.b64decode(ls_f)
                    name = "D:\\Lavinian\\" + str(num) +".jpg"
                    with open(name, 'wb') as f:
                        f.write(imgdata)
                    print(str(num)+"下载成功")
                    #time.sleep(1)
                    num+=1
            #print(content1)








if __name__ == '__main__':
    index()