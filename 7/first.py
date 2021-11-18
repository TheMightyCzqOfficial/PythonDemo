from bs4 import BeautifulSoup
import requests
class No1(object):

    def geturl(self):

        url = "https://search.sina.com.cn/?q=%E6%95%99%E8%82%B2&range=all&c=news&sort=time"
        res = requests.get(url)
        content = res.content.decode(res.apparent_encoding)
        soup = BeautifulSoup(content,"html.parser")
        result = soup.find_all(class_="box-result clearfix")
        #print(content)
        #print(result)


        for i in result:
            none = i.h2.a.string
            if(none==None):
             print(i.h2.a)
            else:
             print(i.h2.a["href"]+i.h2.a.string)
        return





if __name__ == "__main__":
    spider = No1()
    spider.geturl()
