yuju=[59,60,71,99,101]
panduan=[59,61,75,95,1011,-9]
def run():
    print("语句覆盖： ")
    for i in yuju:
        test(i)
    print("判断覆盖： ")
    for i in panduan:
        test(i)
def test(a):
    if(a>=60 and a<=100):
        if(a<70):
            print("分数为："+str(a)+"  及格 ")
        if(a>=70 and a<90):
            print("分数为："+str(a)+"  良 ")
        if(a<=100 and a>=90):
            print("分数为："+str(a)+"  优秀 ")
    else:
        if(a<60 and a>=0):
            print("分数为："+str(a)+"  不及格 ")
        else:
            print("分数为："+str(a)+"  输入有误请重新输入！ ")
if __name__=='__main__':
   run()