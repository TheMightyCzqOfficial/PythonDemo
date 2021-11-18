from 农业数据.GetProduct import GetInfo
from 农业数据.GetPrice import main
#database文件修改用户名，密码，数据库，运行sql文件建表
def run():
    print("是否更新农产品代码？ Y/N \n")
    a=input()
    if a=="Y":
        GetInfo()
    elif a=="N":
        main()
    else:
        print("输入有误请重新输入\n")
        run()

if __name__ == '__main__':
    run()
