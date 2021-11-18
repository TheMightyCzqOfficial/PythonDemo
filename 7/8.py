import requests
from bs4 import BeautifulSoup
import jieba
import jieba.analyse as anle
import jieba.posseg as plse


class No2(object):
    model = ["产业","教育","艺术"]
    def __init__(self):
        return

    def show(self):
        resp = requests.get("https://www.mju.edu.cn/2020/1116/c27a100488/page.htm")
        content = resp.content.decode(resp.apparent_encoding)
        soup = BeautifulSoup(content,"html.parser")
        result = soup.select_one(".wp_articlecontent").children
        data = []
        for node in result:
            data.append(node.text)
        txt = "".join(data)
        result = jieba.cut_for_search(txt)
        print("/".join(result))
        keywords = anle.textrank(txt,topK=20, withWeight=True)
        kw = []
        for x in keywords:
            kw.append(x[0])

        inter = set(self.model).intersection(kw)
        sim = len(inter)/(len(self.model)+len(kw)-len(inter))

        print(sim)
        return

    def testjb(self):
        info = "由闽江学院、漆树产业国家创新联盟共同主办"
        result = jieba.cut(info,True)
        print("/".join(result))

if __name__ == "__main__":
    spider = No2()
    spider.show()
    #spider.testjb()