import chardet
import requests

def show():
    res = requests.get("http://www.mju.edu.cn")
    cs = chardet.detect(res.content)
    print(cs['encoding'])

if __name__ == '__main__':
    show()