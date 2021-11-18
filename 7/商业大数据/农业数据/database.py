import pymysql

#数据库：用户名 密码 数据库名
user="root"
pw="chen2000624."
database="product"
def AddIntoProduct_data(code):

    conn = pymysql.connect(host='localhost', port=3306, user=user, passwd=pw, db=database,
                           charset="utf8")
    cursor = conn.cursor()
    add = "insert ignore into product_data values('"+str(code[0])+"','"+str(code[1])+"','"+str(code[2])+"','"+str(code[3])+"')"

    try:
        {
                cursor.execute(add),
                print("添加信息成功！")
        }
    except:
            {
                print("添加错误！")
            }

    conn.commit()
    cursor.close()
    conn.close()

def AddIntoProduct(code):

    conn = pymysql.connect(host='localhost', port=3306, user=user, passwd=pw, db=database,
                           charset="utf8")
    cursor = conn.cursor()
    add = "insert ignore into product values('"+str(code[0])+"','"+str(code[1])+"','"+str(code[2])+"')"

    try:
        {
                cursor.execute(add),
                print("添加信息成功！")
        }
    except:
            {
                print("添加错误！")
            }

    conn.commit()
    cursor.close()
    conn.close()

def SelectProduct(what,table,result,condition):
    conn = pymysql.connect(host='localhost', port=3306, user=user, passwd=pw, db=database,
                           charset="utf8")
    cursor = conn.cursor()
    select = "select {0} from {1} where {2}='{3}' ".format(what,table,result,condition)
    print(select)
    try:
        {
            cursor.execute(select)
        }
    except:
        {
            print("查询错误！")
        }
    last_id = cursor.fetchall()

    print("结果如下: \n")
    for i in last_id:
        print(i)
    return last_id
    cursor.close()
    conn.close()

def select(table):
    conn = pymysql.connect(host='localhost', port=3306, user=user, passwd=pw, db=database,
                           charset="utf8")
    cursor = conn.cursor()
    select = "select * from %s order by id desc" % table
    try:
        {
            cursor.execute(select)
        }
    except:
        {
            print("查询错误！")
        }
    last_id = cursor.fetchall()

    print("表名: " + table + " 如下:\n")
    for i in last_id:
        print(i)
    return last_id
    cursor.close()
    conn.close()

def selectBySQL(SQL):
    conn = pymysql.connect(host='localhost', port=3306, user=user, passwd=pw, db=database,
                           charset="utf8")
    cursor = conn.cursor()
    select =str(SQL)
    try:
        {
            cursor.execute(select)
        }
    except:
        {
            print("查询错误！")
        }
    last_id = cursor.fetchall()

    print(str(SQL)+" 结果如下:\n")
    for i in last_id:
        print(i)
    return last_id
    cursor.close()
    conn.close()
if __name__=="__main__":
    #AddIntoProduct()
    select(input())