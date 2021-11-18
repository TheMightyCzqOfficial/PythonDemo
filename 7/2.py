import jieba
import requests
from link import get
from bs4 import BeautifulSoup
topicword=["主办","海洋","白痴","坏蛋","傻瓜","笨蛋"]
link=get()
class No2(object):
    def __init__(self):
        return

    def show(self):

        for i in link:
            resp = requests.get(link[i])
            content = resp.content.decode(resp.apparent_encoding)
            soup = BeautifulSoup(content,"html.parser")
            result = soup.select_one(".wp_articlecontent").children
            data = []
            for x in result:
                data.append(x.text)
            txt = "".join(data)
            result = jieba.lcut_for_search(txt)

            commonWord = set(topicword).intersection(result)

            if (commonWord==set()):
                print('未发现')
            else:
                print("发现关键词："+str(commonWord)+link[i])








if __name__ == "__main__":
    spider = No2()
    spider.show()