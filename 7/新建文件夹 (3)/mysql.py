import pymysql
import re
#create database python_final;create table test (id int(10) zerofill);
#create table code(code int(10) zerofill);
#conn = pymysql.connect(host='localhost',port=3306,user = "root",passwd = "chen2000624.",db = "python_final",charset="utf8")
#cursor = conn.cursor()
def add(data):
    conn = pymysql.connect(host='localhost', port=3306, user="root", passwd="chen2000624.", db="python_final",
                           charset="utf8")
    cursor = conn.cursor()
    add = "insert into code values('%s')"%data
    try:
        {
                cursor.execute(add),
                print("添加成功！")

        }
    except:
            {
                print("添加错误！")
            }
    conn.commit()
    selectall()
    cursor.close()
    conn.close()
def selectall():
    conn = pymysql.connect(host='localhost', port=3306, user="root", passwd="chen2000624.", db="python_final",
                           charset="utf8")
    cursor = conn.cursor()
    select = "select * from code "
    try:
        {
                cursor.execute(select)
        }
    except:
            {
                print("查询错误！")
            }
    last_id = cursor.fetchall()
    result = re.findall('\d{6}',str(last_id))
    print("股票代码:")
    for i in result:
        print(i)
    return result
    cursor.close()
    conn.close()
def delete(code):
    conn = pymysql.connect(host='localhost', port=3306, user="root", passwd="chen2000624.", db="python_final",
                           charset="utf8")
    cursor = conn.cursor()
    delete = "delete from code where code = %s"%code
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
    selectall()

    cursor.close()
    conn.close()


if __name__=="__main__":
    selectall()
    #add(input("输入要添加的股票代码:"))
    delete(input("输入要删除的股票代码:"))
    selectall()

