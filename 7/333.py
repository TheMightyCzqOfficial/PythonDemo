import requests
import re
import base64
from io import BytesIO
import time
import os

def show():
    header = {

         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400"
     }
    url0="https://dymnt.com/zt/gebi/"
    res = requests.get(url0, headers=header)
    content = res.content.decode(res.apparent_encoding)
    total = re.findall('<div class="pin-coat"> <a href="(.*?)" class="', content)
    for i in total[19:]:
        url1="https://dymnt.com/"+i
        res = requests.get(url1, headers=header)
        content = res.content.decode(res.apparent_encoding)
        mingzi=re.findall('<h2 class="main-title">(.*?)</h2>',content)
        urls = re.findall('<a class="page-numbers" title="Page">&nbsp;<b>(.*?)</b', content)
        #print(urls)
        pagenum = re.findall('\d{2}',str(urls))
        num=pagenum[0]
        biaoti=mingzi[0]
        os.mkdir("D:\srww3\\"+biaoti)
        print("标题:"+biaoti+"  共"+num+"页")
        print("开始下载---------------------------------")
        num=eval(num)
        i1=i.replace(".html","")
        print(i1)
        # print(type(num))
        #print(num)
        a=2
        for i in range(num):
            print("开始下载第"+str(a)+"页")
            url="https://dymnt.com"+i1+"_"+str(a)+".html"
            #print(url)
            res=requests.get(url,headers=header)
            content1 = res.content.decode(res.apparent_encoding)
           # print(content1)  <img  src='
            urls = re.findall('<img  src="(.*?)" alt=', content1)
            urls1=re.findall('<img src=\'(.*?)\'', content1)
            urls2=re.findall('<img  src=\'(.*?)\'', content1)
            #print(str(urls1))
            #print(str(urls))
            #print(str(urls2))
            if(str(urls)=="[]" and str(urls1)=="[]"):
                aa=urls2[0]
                bb=aa.replace("https://img.dymnt.com/","")
                cc="https://img.dymnt.com/"+bb
                r = requests.get(cc, headers = header)
            if(str(urls)=="[]" and str(urls2)=="[]"):
                aa = urls1[0]
                bb = aa.replace("https://img.dymnt.com/", "")
                cc = "https://img.dymnt.com/" + bb
                r = requests.get(cc, headers=header)
            if(str(urls1)=="[]" and str(urls2)=="[]"):
                aa = urls[0]
                bb = aa.replace("https://img.dymnt.com/", "")
                cc = "https://img.dymnt.com/" + bb
                r = requests.get(cc, headers=header)
            #print(r.content)
            #image = Image.open(BytesIO(r.content))
            ls_f = base64.b64encode(BytesIO(r.content).read())
            imgdata = base64.b64decode(ls_f)
            name = "D:\\srww3\\"+biaoti+"\\"+biaoti+"  "+str(a)+".jpg"
            with open(name,'wb') as f:
                f.write(imgdata)
            print("共" + str(num) + "页   第"+str(a)+"页下载成功")
            time.sleep(1)
            a = a + 1
            if(a==num):
                print("下载完成!!")
                break

    print("全部下载完成!!")



if __name__=="__main__":

   show()


