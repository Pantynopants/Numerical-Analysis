# -*- coding: utf-8 -*-
import matplotlib.pyplot as mpl
import numpy as np
import scipy as sp
# http://wenku.baidu.com/link?url=KtOKobewIlc6SJDlY5faeLRPhkxsZYIvGeDrLq59669TVaLZ21VWYkWqfbBYvmqFEBtzZPX58pcWTHvDAK_hgWatlfcDaNuvy4HMoiszh13
# http://wenku.baidu.com/link?url=YmhFSfAigUOOd4nmxOq_1ZurlhHkesSzFUrYIhXdAdTqDAOMJ8mAHIqIzL3wRgF648zg7T_A4NEGH5ISTN_BC54WayWnxe8fiTz2r_pwbpy
# def getdata():
#     a = np.zeros(10,np.double)
#     b = np.zeros(10,np.double)
#     for i in range(len(a)):
#         a[i] = np.random.uniform(-255,255)
#         b[i] = np.random.uniform(-255,255)
#         print '(%f,%f)' %(a[i],b[i]),
#     print 
#     return a,b 

# a = [0.4, 0.55, 0.65, 0.80, 0.95, 1.05]
# b = [0.41075, 0.57815, 0.69675, 0.90, 1.00, 1.25382]

a = [1, 2, 3, 4, 5, 6, 7]
b = [0.368, 0.135, 0.050, 0.018, 0.007, 0.002, 0.001]

temp = a[0:6]
print temp
# a = np.array([-2,2,5],np.float32)
# b = np.array([0,3,6],np.float32)
L = []
# 构造插值多项式L1L2等
def createL(x,value):
    # L = [1 for i in range(0,len(x))]
    del L[:]
    for i in xrange(0,len(x)):
        L.append(1)
    
    # print L
    # 对于5次和6次，不满6次的不存在,以此类推
    for j in xrange(0, len(x)):
        for i in range(0, len(x)):
            if i == j:
                continue
            else:
                L[j] *= (value-x[i])/(x[j]-x[i])



# print L
# def Lar(x,y,a):
#     #t = np.zeros(len(a))
#     #t = a.copy()
#     ans = 0.0
#     for i in range(len(y)):
#         t = y[i]
#         for j in range(len(L)):
#             if i != j:
#                 t *= (a-x[j])/(x[i]-x[j])
#         ans += t
#     return ans

# y2 = Lar(a,b,0.596)
# print y2
# y3 = Lar(a,b,0.99)
# print y3
# mpl.plot(a,b,'--*')

def Larange(x,y,value):
    #t = np.zeros(len(a))
    #t = a.copy()
    createL(x, value)
    print L
    ans = 0.0
    for i in range(len(x)):
        index = a.index(x[i])
        t = y[index]
        
        t *= L[i]
        ans += t
    return ans

y2 = Larange(a,b,0.596)
print u"x=0.596 Larange插值为%s" %y2
y3 = Larange(a,b,0.99)
print u"x=0.99 Larange插值为%s" %y3
mpl.plot(a,b,'--*')



def Fenduan2(x, y, value):
    F = []
    del F[:]
    for i in xrange(0,len(x)-1):
        if value >= x[i] and value <= x[i+1]:
            print "in fenduan"
            print x[i],x[i+1]
            if abs(value-x[i]) > abs(x[i+1] - x[i])/2:
                #get i,i+1,i+2
                if i+2 <= len(x):
                    F = x[i:i+3]
                else: F = x[len(x)-3:len(x)]
            else:
                #get i-1,i,i+1
                if i+1 <= len(x):
                    F = x[i-1:i+2]
                else: F = x[len(x)-3:len(x)]

    print F
    ans = Larange(F,y,value)
    return ans

y2 = Fenduan2(a,b,0.596)
print u"x=0.596 分段二次插值为%s" % y2
y3 = Fenduan2(a,b,0.99)
print u"x=0.99 分段二次插值为%s" % y3

# y4 = Larange(a,b,1.8)
# print u"Larange插值为%s" % y4
# y5 = Fenduan2(a,b,1.8)
# print u"三点插值为%s" % y5

def Fenduan(x, y, value):
    F = []
    del F[:]
    for i in xrange(0,len(x)-1):
        if value >= x[i] and value <= x[i+1]:
            if i+1 <= len(x):
                F = x[i:i+2]
            else: F = x[len(x)-2:len(x)]
            
    print u"F is:"
    print F
    ans = Larange(F,y,value)
    return ans

# y6 = Fenduan(a,b,1.8)
# print u"二点插值为%s" % y6

mpl.show()
