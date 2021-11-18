import requests
from bs4 import BeautifulSoup

def origin(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400"
    }
    res = requests.get(url, headers=header)
    content = res.content.decode(res.apparent_encoding)
    #print(content)
    return content
def run(url,text):
    soup = BeautifulSoup(origin(url), "html.parser")
    result = soup.find_all(class_=text)
    print(result)
    return result
if __name__=="__main__":
    run("column-news-item")