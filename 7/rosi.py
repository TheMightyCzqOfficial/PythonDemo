#http://www.chaomb.com/30/3555-6419.html?page=1
import requests
import re
import base64
from io import BytesIO
import time
import os

from bs4 import BeautifulSoup


def run():
    ii=2
    index()
    for i in range(29):
        url="https://www.uu131.net/meinv/MFStar/list_42_"+str(ii)+".html"
        second(url)
        ii+=1
def index():
    header = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }
    proxies = {

        'http':'175.42.122.182:9999'

    }
    worker_session = requests.Session()
    url0 = "https://www.uu131.net/meinv/MFStar/index.html#"
    res = worker_session.get(url0, proxies=proxies, verify=False, stream=True, headers=header)

    #res = requests.get(url0,headers=header)
    res=res.text
    #content = res.content.decode(res.apparent_encoding)
    total = re.findall("<a href=\"(.*?)\"  target=", res)
   #
    #print(img)
    print(total)
    for i in total:
        i1 = i.replace(".html", "")
        a=1
        b=2
        url=i
        res = requests.get(url, headers=header)
        #content = res.content.decode(res.apparent_encoding)
        res = res.text
        # content = res.content.decode(res.apparent_encoding)
        content = re.findall("<a href=\"(.*?)\"  target=", res)
        soup = BeautifulSoup(content, "html.parser")
        page=re.findall("共(.)页",content)
        page0=int(page[0])
        result = soup.find_all(class_="content")
        #s=str(result)
        s = re.findall("src=\"(.*?)\"", str(result))
        mingzi=re.findall("alt=\"(.*?)\"", str(result))
        biaoti = mingzi[0]
        os.mkdir("D:\\ru1mm\\" + biaoti)
        print("标题:" + biaoti +"   共"+page[0]+"页")
        for img in s:#first page
            r=requests.get(img, headers=header)
            ls_f = base64.b64encode(BytesIO(r.content).read())
            imgdata = base64.b64decode(ls_f)
            name = "D:\\ru1mm\\" + biaoti + "\\" + biaoti + "  " + str(a) + ".jpg"
            with open(name, 'wb') as f:
                f.write(imgdata)
            print("下载成功")
            time.sleep(1)
            a+=1
        print("---------------------------")
        for p in range(page0-1):#next page
            print("进入第"+str(b)+"页")
            url1 = i1 + "_" + str(b) + ".html"
            res = requests.get(url1, headers=header)
            content = res.content.decode(res.apparent_encoding)
            soup = BeautifulSoup(content, "html.parser")
            result = soup.find_all(class_="content")
            s1 = re.findall("src=\"(.*?)\"", str(result))
            for img1 in s1:
                r = requests.get(img1, headers=header)
                ls_f = base64.b64encode(BytesIO(r.content).read())
                imgdata = base64.b64decode(ls_f)
                name = "D:\\ru1mm\\" + biaoti + "\\" + biaoti + "  " + str(a) + ".jpg"
                with open(name, 'wb') as f:
                    f.write(imgdata)
                print("下载成功")
                time.sleep(1)
                a += 1
            b+=1
        print(biaoti+"下载完成")

def second(url0):
    header = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400"
    }
    proxies = {

        'http':'112.80.248.75:80'

    }
    worker_session = requests.Session()
    res = worker_session.get(url0, proxies=proxies, verify=False, stream=True, headers=header)
    content = res.content.decode(res.apparent_encoding)
    total = re.findall("<a href=\"(.*?)\"  target=", content)
   #
    #print(img)
    print(total)
    for i in total:
        i1 = i.replace(".html", "")
        a=1
        b=2
        url=i
        res = requests.get(url, headers=header)
        content = res.content.decode(res.apparent_encoding)
        soup = BeautifulSoup(content, "html.parser")
        page=re.findall("共(.)页",content)
        page0=int(page[0])
        result = soup.find_all(class_="content")
        #s=str(result)
        s = re.findall("src=\"(.*?)\"", str(result))
        mingzi=re.findall("alt=\"(.*?)\"", str(result))
        biaoti = mingzi[0]
        os.mkdir("D:\\ru1mm\\" + biaoti)
        print("标题:" + biaoti +"   共"+page[0]+"页")
        for img in s:#first page
            r=requests.get(img, headers=header)
            ls_f = base64.b64encode(BytesIO(r.content).read())
            imgdata = base64.b64decode(ls_f)
            name = "D:\\ru1mm\\" + biaoti + "\\" + biaoti + "  " + str(a) + ".jpg"
            with open(name, 'wb') as f:
                f.write(imgdata)
            print("下载成功")
            time.sleep(1)
            a+=1
        print("---------------------------")
        for p in range(page0-1):#next page
            print("进入第"+str(b)+"页")
            url1 = i1 + "_" + str(b) + ".html"
            res = requests.get(url1, headers=header)
            content = res.content.decode(res.apparent_encoding)
            soup = BeautifulSoup(content, "html.parser")
            result = soup.find_all(class_="content")
            s1 = re.findall("src=\"(.*?)\"", str(result))
            for img1 in s1:
                r = requests.get(img1, headers=header)
                ls_f = base64.b64encode(BytesIO(r.content).read())
                imgdata = base64.b64decode(ls_f)
                name = "D:\\ru1mm\\" + biaoti + "\\" + biaoti + "  " + str(a) + ".jpg"
                with open(name, 'wb') as f:
                    f.write(imgdata)
                print("下载成功")
                time.sleep(1)
                a += 1
            b+=1
        print(biaoti+"下载完成")




   # os.mkdir("D:\\rosi\\" + "第"+str(num)+"期")

if __name__ == "__main__":
        run()
       # ran()