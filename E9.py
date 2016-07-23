# -*- coding: utf-8 -*-

from math import *
'定义被积分函数'

def func(x): 
    return sqrt(4 - ((sin(x))**2))
# def func(x):
#     return x**3
# func(x)=x**3
# def func(x):
#     if x == 0:
#         return 1
#     return sin(x)/x

def Get_N(a,b,width):
    # width为步长 n为迭代次数
    N = int((b-a)/width + 1)#向上取整
    if N%2 == 0:
        N = N + 1
    return N

def GenerateData(a,b,n,width):
    datas = []
    r = a
    for i in range(0,n):
        datas.append(func(r))
        r = r+width
        # print r
    return datas

def NC_integral(datas,width,n):
    sum = datas[0]+datas[n-1]
    for i in range(2,n):
        sum = sum + 2*datas[i-1]
    return sum*width/2.0

def simpson_integral(datas,width,n):
    sum = datas[0]+datas[n-1]
    for i in range(2,n):
        if i%2 == 0:
            sum = sum + 4*datas[i-1]#奇数
        else:
            sum = sum + 2*datas[i-1]#偶数
    return sum*width/3.0

def Romberg(a, b, e, m):
    # a,b 积分上下限 e精度 m最大次数
    RT = []
    n = 1
    h = b-a
    # 误差估计
    wugu = 1
    x = a
    k = 0

    for i in range(0, 4):
        tmp = []
        for j in range(0, 4):
            tmp.append(0)
        RT.append(tmp)
    print RT

    RT[0][0] = h*(func(b) + func(a))/2
    while (wugu > e and k < m) and k<=2:
        # print k
        k += 1
        h /= 2.0
        s = 0.0
        for j in xrange(1,n):
            x = a + h*(2.0*j - 1.0)
            s += func(x)

        
        RT[k][0] = RT[k-1][0]/2 + h*s
        n *= 2
        for i in xrange(1,k+1):
            RT[k][i] = ( (4.0**i) * RT[k][i-1] - RT[k-1][i-1])/(4.0**i - 1.0)
        wugu = abs(RT[k][k-1] - RT[k][k])

    print k
    return RT[k][k]

if __name__ == "__main__":
    a = 0.0 #积分下限
    b = pi/4
    h = 0.0625 #步长
    # 

    h = (b-a)/10
    # print func(0)
    N = Get_N(a,b,h)
    # print N
    datas = GenerateData(a,b,N,h)
    print datas
    print simpson_integral(datas,h,N)
    print NC_integral(datas,h,N)
    print Romberg(0.5, 1, 1e-6, 10)
    print Romberg(1, 2, 1e-6, 10)

    a = 0.0 #积分下限
    b = 1.0 #积分上限
    # h = 0.0625 #步长
    h = (b-a)/10

    N = Get_N(a,b,h)
    # print N
    datas = GenerateData(a,b,N,h)
    print datas
    print simpson_integral(datas,h,N)
    print NC_integral(datas,h,N)
    print Romberg(0.5, 1, 1e-6, 10)
    print Romberg(1, 2, 1e-6, 10)