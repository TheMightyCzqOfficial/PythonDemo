import re
import requests
def get():
   link={}
   for i in range(2):
     a = requests.get("http://www.mju.edu.cn/xxyw/list"+str(i)+".htm")
     info = a.content.decode("utf-8")
     res2 = re.findall('<a class="column-news-item item-\d+ clearfix" href="(.*?)" ',info)
     a=0
     for item in res2:
         link[a]=('http://www.mju.edu.cn'+item)
        # print(link[a])
         a=a+1
   return  link



if __name__ == '__main__':
       print(get())
