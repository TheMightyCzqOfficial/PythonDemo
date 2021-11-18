from 农业数据.ShowapiRequest import ShowapiRequest
import re
import time
from 农业数据.database import AddIntoProduct_data,select,SelectProduct,selectBySQL
def main():
    case=input("请输入需要进行的操作：1.查询并添加到数据库 2.查看数据库的所有内容 3.简单条件查询\n")
    if(eval(case)==1):
        check()
    elif(eval(case)==2):
        selectAll()
    elif(eval(case)==3):
        selectByInfo()
    else:
        print("输入有误,请重新输入")
        main()
def check():
    r = ShowapiRequest("http://route.showapi.com/2261-3","662836","7ea7286028714960af10da5bfef4294e" )
    pro=input("请输入查询的省 例如：广东\n")
    city=input("请输入查询的城市 例如：广州\n")
    genus=input("请输入需要添加的品种 畜产/水产/粮油/果品/蔬菜 \n")
    print("即将查询的是 "+str(pro)+"省"+str(city)+"市 的 "+str(genus)+" 价格"+",若该地区无货则自动跳过\n")
    time.sleep(1)
    print("------------------------3--------------------------")
    time.sleep(1)
    print("------------------------2--------------------------")
    time.sleep(1)
    print("------------------------1--------------------------")
    time.sleep(1)
    id=SelectProduct('id','product','genus',genus)
    for code in id:
        print(code[0])
        r.addBodyPara("pro", pro)
        r.addBodyPara("city", city)
        r.addBodyPara("code", code[0])
        res = r.post()
        #print(res.text) # 返回信息

        money=re.findall("\"money\":(.*?),\"",res.text)
        add=re.findall("\"address\":\"(.*?)\"",res.text)
        date=re.findall("\"date\":\"(.*?)\"",res.text)
        #print(money)
        #print(add)
        #print(date)
        if str(money)=="[]":
            print("该地区无此货物")
            time.sleep(0.5)
            continue
        else:
            num=0
            print("------------自动添加至数据库表 product_data------------")
            time.sleep(1)
            print("------------------------3--------------------------")
            time.sleep(1)
            print("------------------------2--------------------------")
            time.sleep(1)
            print("------------------------1--------------------------")
            time.sleep(1)
            for i in money:
                data=[]
                data.append(code[0])
                data.append(i+" 元/斤")
                data.append(add[num])
                data.append(date[num])
                num+=1
                print(data)
                AddIntoProduct_data(data)
    print("--------------全部添加完毕--------------")
    main()
def selectAll():
    table=input("请输入查询的表名 product/product_data \n")
    select(table)
    time.sleep(0.5)
    print("--------------查询完毕------------------")
    main()
def selectByInfo():
    selectBySQL(input("请输入SQL查询语句,例如:SELECT * FROM product\n"))
    main()
if __name__=="__main__":
    main()