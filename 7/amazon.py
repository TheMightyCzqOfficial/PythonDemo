from bs4 import BeautifulSoup
import requests

def geturl(text):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400"
        ,"Cookie": "session-id=459-7246415-9774300; ubid-acbcn=458-1434102-4876968; session-token=M0gj4X+u3X2okndL4UvMDrxnQTtZYq6rx8nTAK20Wdcz8dR0W0ZB5rhlNfIkbAlABI1rEMnlfOzQA39IBTfryg0WXQDn0z33Cq9v6ydEs8WeIM1+iFs5e740aKAuPJm9UBpR4dfU8cjMxu+YZGgYcZSBCWehJyt+TIOHQy3nMhFUodAg3G3q6Wj3iyt0mQLA; session-id-time=2082729601l; csm-hit=tb:N66VBBT9MHVWYXFPVS5D+s-HATMH8H7ZFS58W5Q6FTT|1609351051871&t:1609351051871&adb:adblk_no"
        }
        proxies = {
            'http': '222.189.190.161:9999'
        }
        #url = "https://www.amazon.cn/s?k="+str(a)+"&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&ref=nb_sb_noss"
        url = "https://www.amazon.cn/s?k="+str(text)+"&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=XCDR4FD6TIZP&sprefix=xianka%2Caps%2C207&ref=nb_sb_ss_ts-a-p_1_6"
        a=[]
        a1=[]
        b=0
        c=[]
        worker_session = requests.Session()
        #res = worker_session.get(url, proxies=proxies,verify=False, stream=True, headers=header,timeout=5)
        res = requests.get(url,headers=header)
        content = res.content.decode(res.apparent_encoding)
        soup = BeautifulSoup(content,"html.parser")
        result = soup.find_all(class_="a-section a-spacing-medium")
        result2= soup.find_all(class_="a-price")
        result3 = soup.find_all(class_="a-link-normal a-text-normal")
        for i in result3:
            a1.append(i.get('href'))

        for i in result2:
           a.append(i.span.string)

        for i in result:
            c.append('名称：'+i.h2.span.string+'  价格：'+a[b]+'  链接：https://www.amazon.cn'+a1[b])
           # print('名称：'+i.h2.span.string+'  价格：'+a[b]+'  链接：https://www.amazon.cn'+a1[b])
            b=b+1
        str1 = str(c)
        print(str1.replace("'", "\n"))
        return str1.replace("'","\n")





if __name__ == "__main__":

   geturl("显卡")
