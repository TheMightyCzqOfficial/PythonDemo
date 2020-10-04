import requests
import chardet
from bs4 import BeautifulSoup
import re

def showInfo():
    res = requests.get("http://finance.sina.com.cn/roll/index.d.html?cid=56589&page=1")
    cs = chardet.detect(res.content)
    # print(cs)
    s = res.content.decode("utf-8")
    # print(s)
    # s1 = res.content.decode("gbk")
    # print(s1)
    # soup = BeautifulSoup(s, features="lxml")
    print(res.content.decode('utf-8'))
    result = re.findall('https://([0-9a-z/\.\-]*)',res.content.decode('utf-8'))
    for item in result:
        print(item)
    cont = re.findall('<a.*?href=".*?">.*?</a>', res.content.decode("utf-8"))
    for it in cont:
        print(it)

def retest():
    info = "dfagaasdffghasdfdfdfgh"
    result = re.findall('a*',info);
    print(result)


def validate_email():
    info = "kk.course_prev@mju.edu.cn"
    ret = re.findall('(.*)@', info)
    print(ret)

if __name__ == '__main__':
    validate_email()