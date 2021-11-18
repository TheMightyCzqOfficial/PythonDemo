import requests
import re

def run():
    word=["CPU","ALU","SISD","SIMD","MISD","MIMD","ROM","RAM"]
    mean=[]
    for i in word:
        url="http://www.iciba.com/word?w="+i
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400"
        }
        res=requests.get(url,headers=header)
        content = res.content.decode(res.apparent_encoding)
        zh=re.findall("</i><div><span>(.*?)<!-- -->",content)
        mean.append(zh[0])
        #print(content)
    for i in mean:
        print(i)


if __name__ == '__main__':
    run()