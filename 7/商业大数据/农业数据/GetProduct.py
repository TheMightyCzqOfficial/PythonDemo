from 农业数据.ShowapiRequest import ShowapiRequest
import re
import time
from 农业数据.database import AddIntoProduct,select
def GetInfo():
    r = ShowapiRequest("http://route.showapi.com/2261-1","662836","7ea7286028714960af10da5bfef4294e" )
    number=1
    for i in range(5):
       # r.addBodyPara("name", "菜")
        r.addBodyPara("genus_code", number)
        number+=1
        res = r.post()
        #print(res.text) # 返回信息
        code=re.findall("\"code\":\"(.*?)\"",res.text)
        name=re.findall("\"name\":\"(.*?)\"",res.text)
        genus=re.findall("\"genus\":\"(.*?)\"",res.text)
        print(code)
        print(name)
        print(genus)
        num=0
        print("------------自动添加至数据库表 product---------------")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        for i in code:
            data=[]
            data.append(i)
            data.append(name[num])
            data.append(genus[num])
            num+=1
            AddIntoProduct(data)
            print(data)
        print("--------------全部添加完毕--------------")
    table=input("请输入查询的表名 product/product_data \n")
    select(table)
    time.sleep(0.5)
    print("--------------查询完毕------------------")

if __name__ == '__main__':
    GetInfo()