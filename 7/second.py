from bs4 import BeautifulSoup
import requests
import re
import xlwt
class No2(object):
    def show(self):
        workbook = xlwt.Workbook(encoding='ascii')
        worksheet = workbook.add_sheet('My Worksheet')
        list=[]
        url = "http://search.sina.com.cn/?q=%BD%CC%D3%FD&c=news&from=channel"
        res = requests.get(url)
        content = res.content.decode(res.apparent_encoding)
        soup = BeautifulSoup(content, "html.parser")
        result = soup.find_all(class_="box-result clearfix")

        a = 0
        for i in result:
            s = " "
            url = i.h2.a["href"]
            print(url)
            res = requests.get(url)
            content = res.content.decode(res.apparent_encoding)
            soup = BeautifulSoup(content,"html.parser")
            #print(content)
            #print(soup)
            date = soup.find(class_="date")
            if((re.search(".*detail",url))!=None):
                continue
            else:
             result = soup.find(class_="article").find_all('font')
             result2 = soup.find(class_="article").find_all('p')
            #print(result2)
            print("日期:")
            worksheet.write(a, 1, label=date.text)
            print(date.text)
            print('标题:')
            worksheet.write(a, 0, label=soup.find(class_='main-title').text)
            print(str(soup.find(class_='main-title').text))
           # print(result)
            if(result == list):
                 result_final = result2
                # print("result2")
            if(result!=list and result2!=list):
                result_final = result2
               # print("result1 and 2")
            if(result2 == list):
                result_final = result
               # print("result1")
            print("内容:")
            for i in result_final:
               s+=i.text
               print(i.text)

            worksheet.write(a, 3, label=s)


            a=a+1
            workbook.save('Excel_Workbook.xls')








if __name__ == "__main__":
    spider = No2()
    spider.show()
