# -*- coding: utf-8 -*-
from numpy import *
import scipy.linalg as linalg
import matplotlib.pyplot as plt

def m1(x):
    print "in function 1"
    if x == 0:
        return 0
    return (3*x + 1.0)/x**2

def m2(x):
    print "in function 2"
    return (x**3 - 1.0)/3.0

def m3(x):
    print "in function 3"
    return (3*x + 1.0)**(1./3)  

def m4(x):
    print "in function 4"
    return (x**2 - 3.0)**(-1)

def m5(x):
    print "in function 5"
    return ( 3 + 1/x)*(1./2)

def m6(x):
    print "in function 6"
    return (x - (x**3 - 3*x - 1)/(3*x**2 - 3))

def easy(methods, x0, e):
    # print 3.0**(-1)

    x = x0
    x1 = 0.0
    # func = {1:m1, 2:m2, 3:m3}
    # func[2](x)
    func = [m1, m2, m3, m4, m5, m6]
    ploty = []
    plotx = []

    delta = 10.0 #为当前精度
    k = 0 #循环次数
    k_max = 100 #最大循环次数

    plt.figure(1)
    '误差大于精度要求 和 x1与x的差不太大时，循环'
    while ((delta > e) and fabs(delta) < 1000):
        x1 = func[methods](x)
        print x1, x, delta
        ploty.append(x)
        plotx.append(k)
        delta = fabs(x1 - x)
        x = x1
        
        if k >= k_max: return x1
        k += 1

    plt.plot(plotx, ploty)
    plt.show()

if __name__ == '__main__':
    #函数入口
    # easy(0, 1.5, 1e-3)
    # easy(1, -1.5, 1e-3)
    # easy(2, 0.0, 1e-3)
    # easy(3, -1.6, 1e-3)
    easy(4, -1.8, 1e-3)
    # easy(5, -1.5, 1e-3)