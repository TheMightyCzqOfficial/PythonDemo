import pymysql
import re
#建表语句：
#create database python_final;
#create table data(code char(6),name char(20),area char(10),sort char(20),year char(20),total char(20));
def select_one(code):
    conn = pymysql.connect(host='localhost', port=3306, user="root", passwd="chen2000624.", db="python_final",
                           charset="utf8")
    cursor = conn.cursor()
    select = "select * from data where code=%s"%code
    try:
        {
            cursor.execute(select)
        }
    except:
        {
            print("查询错误！")
        }
    last_id = cursor.fetchall()

    print("股票:")
    for i in last_id:
        print(i)
    cursor.close()
    conn.close()
    #print(type(str((last_id))))
    return last_id

def selectstock():
    conn = pymysql.connect(host='localhost', port=3306, user="root", passwd="chen2000624.", db="python_final",
                           charset="utf8")
    cursor = conn.cursor()
    select = "select * from data order by name desc"
    try:
        {
            cursor.execute(select)
        }
    except:
        {
            print("查询错误！")
        }
    last_id = cursor.fetchall()

    print("股票:")
    for i in last_id:
        print(i)
    return last_id
    cursor.close()
    conn.close()
def addstock(code):
  from get_stocks import insert
  a=insert(code)

  for i in a:
    conn = pymysql.connect(host='localhost', port=3306, user="root", passwd="chen2000624.", db="python_final",
                           charset="utf8")
    cursor = conn.cursor()
    add = "insert ignore into data values('"+str(i[0])+"','"+str(i[1])+"','"+str(i[2])+"','"+str(i[3])+"','"+str(i[4])+"','"+str(i[5])+"')"

    try:
        {
                cursor.execute(add),
                print("添加股票成功！")
        }
    except:
            {
                print("添加股票错误！")
            }
    conn.commit()
  selectstock()

  cursor.close()
  conn.close()
def deletestock(code):
    conn = pymysql.connect(host='localhost', port=3306, user="root", passwd="chen2000624.", db="python_final",
                           charset="utf8")
    cursor = conn.cursor()
    delete = "delete from data where code = %s" % code
    try:
        {
            cursor.execute(delete),
            print("删除成功！")

        }
    except:
        {
            print("删除错误！")
        }
    conn.commit()
    selectstock()
    cursor.close()
    conn.close()
if __name__=="__main__":
    #select_one(input())
    addstock(input("输入添加的股票代码:"))
    #selectstock()
    #deletestock(input("输入要删除股票的股票代码:"))


