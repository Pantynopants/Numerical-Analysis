# coding=utf-8  
  
''' 
多项式曲线拟合算法 
# [最小二乘法多项式曲线拟合原理](http://blog.csdn.net/jairuschan/article/details/7517773/)
# [在线拟合工具](http://www.atool.org/fitted_curve.php)
# [利用python搞机器学习——最小二乘法](http://lhdgriver.gotoip1.com/%E5%88%A9%E7%94%A8python%E6%90%9E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0-%E6%9C%80%E5%B0%8F%E4%BA%8C%E4%B9%98%E6%B3%95/)
# [wiki](http://wiki.ohugh.com/zh-hans/Python/Modules/Scipy)
# [leastsq函数](https://help.scilab.org/docs/5.4.0/ja_JP/leastsq.html)
# [最小二乘法以及leastsq函数](http://www.cnblogs.com/NanShan2016/p/5493429.html)
'''  
import matplotlib.pyplot as plt  
from math import *
import numpy  
import random  
  
fig = plt.figure()  
ax = fig.add_subplot(111)  
  
'阶数为9阶 n=9=k'
order=9  
'被拟合的点'
xa = []  
ya = [] 
'画图时，点的取值范围和点的密度。根据源数据点进行推断'
start = 1 # -1
end = 367 # 1
step = (start + end)/200.0
# 实验得步长不影响图形的弯曲程度
# 此概念与KDE核密度的宽度不同
# 因为系数a0,a1,a2...已经得到，此处步长只影响画图质量，可随意设置

#生成样例曲线上的各个点 100个
x = numpy.arange(start, end, step)  
# y = [((a*a-1)*(a*a-1)*(a*a-1)+0.5)*numpy.sin(a*2) for a in x]  
y = [((a*a-1)**3 + 0.5)*sin(2*a) for a in x]
#print x
#print y

# print z
# 生成的原曲线
#ax.plot(x,y,color='r',linestyle='-',marker='.')  
#,label="(a*a-1)*(a*a-1)*(a*a-1)+0.5"  
  
#生成的曲线上的各个点随机偏移一下，并放入到xa,ya中去  
i = 0  
##############################
#生成xa ya的源数据点
##############################

'''
for xx in x:  
    yy = y[i]  
    # 偏移宽度(-40%,+40%)
    d = float(random.randint(60,140))/100  
    #ax.plot([xx*d],[yy*d],color='m',linestyle='',marker='.')  
    i += 1  
    xa.append(xx*d)  
    ya.append(yy*d)  
  
'''
d = []
ya = [i for i in range(start, end)]
random.shuffle(ya)
xa = range(start, end)


#d = tuple(zip(xa, ya))
for i in range(len(xa)):
    d.append([xa[i],ya[i]])
# print d
nd = numpy.array(d)


ax.plot(nd[:, 0], nd[:, 1], 'o', color="white", markersize=7, linewidth=3)

# 偏移之后的点图
#ax.plot(xa,ya,color='m',linestyle='',marker='.')  
  
  
#进行曲线拟合  
matA=[]  #整个多项式矩阵
for i in range(0,order+1):  
    matA1=[]  # 每一行
    for j in range(0,order+1):  
        tx=0.0  # 每一列
        for k in range(0,len(xa)):  
            dx = 1.0  #  表示初始
            for l in range(0,j+i):  
                # l为次数，对应一行的不同次的变量
                # 本区域(重复)运行次数越多次数越高
                # 第一次不运行此区域 表示n=dx
                # 最后一次运行 2order次 即为x^2k(或n^2次)
                dx = dx*xa[k]  

            tx += dx  
            # 运行n次(len(xa)次)后，tx为sum(x[i]^2k) 或 n (dx=1运行n次)
        matA1.append(tx)  
    matA.append(matA1)  
  
#print(len(xa))  
#print(matA[0][0])  

# 转化为ndarray
matA = numpy.array(matA)  
  
matB = []  
for k in range(0,order+1):  
    ty = 0.0  
    # 加和n个
    for i in range(0,len(xa)):  
        dy = 1.0  
        # 对于从i=1->n 求 (x[i])^(k-1)
        for l in range(0, k):  
            dy = dy * xa[i]  #dy即为公式中 (x[i])^k
        ty += ya[i] * dy  # 先乘完再加和
    matB.append(ty)  
   
matB = numpy.array(matB)  

# 多元一次 x^k为系数 a为未知数 求线性的a
matAA = numpy.linalg.solve(matA,matB)  
#得到系数矩阵


# 下面画出拟合后的曲线  
# a0 + a1*x + a2*x^2 +...+ ak*x^k

#print(matAA)  
xxa = numpy.arange(start, end, step)  
yya = []  
for i in range(0,len(xxa)):  
    yy = 0.0  
    for j in range(0,order+1):  
        dy = 1.0  
        for k in range(0,j):  
            dy *= xxa[i] # x^k

        # ak*x^k
        dy *= matAA[j]  # matAA[j]即为系数a 
        yy += dy  
    yya.append(yy)  
ax.plot(xxa,yya,color='g',linestyle='-',marker='')  
  
ax.legend()  
plt.show() 