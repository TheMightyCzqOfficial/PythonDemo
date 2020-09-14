import chardet
import requests
from bs4 import BeautifulSoup
import re

res = requests.get("http://www.mju.edu.cn")
#print(res.content)
cs = chardet.detect(res.content)
#print(cs)
# soup = BeautifulSoup(res.content)
# print(soup)
print(res.content.decode("utf-8"))
result = re.findall(r'<a href=["\'](.*?)["\']',res.content.decode("utf-8"))
print(result)