def moling(a):
    b=float(a)
    print(int(b))
def tihuan(a):
    b=a.replace('fuck','****')
    print(b)
def triangle(a,b,c):
    x=int(a)
    y=int(b)
    z=int(c)
    q=(x+y+z)/2
    s=(q*(q-x)*(q-y)*(q-z))**0.5
    print("半周长为："+str(q)+"\n面积为："+str(s))

if __name__=="__main__":

    moling(input())
    tihuan(input())
    triangle(input(),input(),input())