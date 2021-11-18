import json
import pymysql

def run():

    f=open('C:/Users/Administrator/Desktop/CNcity.json','rb')
    t=json.load(f)
    for i in range(200):
        list = []
        list.append(t[i]['pinyin'])
        list.append(t[i]['zip'])
        print(list)
        addinto(list)

def addinto(code):

    conn = pymysql.connect(host='localhost', port=3306, user="root", passwd="chen2000624.", db="weather",
                           charset="utf8")
    cursor = conn.cursor()
    add = "insert ignore into city values('"+str(code[0])+"','"+str(code[1])+"')"

    try:
        {
                cursor.execute(add),
                print("添加成功！")
        }
    except:
            {
                print("添加错误！")
            }
    select()
    conn.commit()
    cursor.close()
    conn.close()
def select():
    conn = pymysql.connect(host='localhost', port=3306, user="root", passwd="chen2000624.", db="weather",
                           charset="utf8")
    cursor = conn.cursor()
    select = "select name from city order by name desc"
    try:
        {
            cursor.execute(select)
        }
    except:
        {
            print("查询错误！")
        }
    last_id = cursor.fetchall()

    print("城市信息:")
    for i in last_id:
        print(i)
    return last_id
    cursor.close()
    conn.close()
def replace(t):
    t=str(t)
    a = t.replace("\'", "")
    a = a.replace("(", "")
    a = a.replace(")", "")
    a = a.replace(",", "")
    return a
if __name__=="__main__":
   # run()
   city_list=select()
   a=replace(city_list[0])
   print(a)