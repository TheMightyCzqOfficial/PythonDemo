import requests
import re

class BilibiliSprite(object):
    __keyword = "default"
    __list_init_url = "http://www.mju.edu.cn/xxyw/list.htm"
    __total_pages = 0
    __all_page_url = []

    def __init__(self, keyword):
        self.__keyword = keyword

    def get_pages(self):
        resp = requests.get(self.__list_init_url)
        content = resp.content.decode(resp.apparent_encoding)
        re_rul = '<em class="all_pages">(\d*)</em>'
        result = re.findall(re_rul, content)
        if result is not None:
            self.__total_pages = result[0]

    def detail_url(self):
        url = "http://www.mju.edu.cn/xxyw/list.htm"
        for i in range(int(self.__total_pages)):
            print("进度" + str(i))
            if i > 1:
                url = "http://www.mju.edu.cn/xxyw/list" + str(i) + ".htm"
            resp = requests.get(url)
            content = resp.content.decode(resp.apparent_encoding)
            page_re_rule = '<a class="column-news-item item-\d* clearfix" href="(.*)" target="_blank"><span class="column-news-title">'
            page_result = re.findall(page_re_rule, content)
            for item in page_result:
                self.__all_page_url.append("http://www.mju.edu.cn" + item)
        print(self.__all_page_url)

    def printinfo(self):
        print(self.__keyword)


if __name__ == '__main__':
    bili = BilibiliSprite("管理")
    bili.get_pages()
    bili.detail_url()
