from bs4 import BeautifulSoup
import requests


class No1(object):
    header = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400"
       }
    proxies = {
        'http': '222.189.190.161:9999',
    }
    url = "https://www.amazon.cn/s?k=%E6%98%BE%E5%8D%A1&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&ref=nb_sb_noss"
    def geturl(self):
        a=[]
        a1=[]
        b=0
        worker_session = requests.Session()
        res = worker_session.get ( self.url,proxies = self.proxies,verify = False,stream = True,headers =self.header,timeout = 5)
        content = res.content.decode(res.apparent_encoding)
        soup = BeautifulSoup(content,"html.parser")
        result = soup.find_all(class_="a-section a-spacing-medium")
        result2= soup.find_all(class_="a-price")
        result3 = soup.find_all(class_="a-link-normal a-text-normal")
       # print(contczqent)
        #print(result3)
        for i in result3:
            a1.append(i.get('href'))
        #print(a1)
        for i in result2:
           a.append(i.span.string)
        for i in result:
            print('名称：'+i.h2.span.string+'  价格：'+a[b]+'  链接：https://www.amazon.cn'+a1[b])
            b=b+1






if __name__ == "__main__":
    spider = No1()
    spider.geturl()