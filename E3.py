# -*- coding: utf-8 -*-
from numpy import *
import scipy.linalg as linalg
from E3_data import *

'A B 为线性方程组, x0为初值,e为精度.返回结果矩阵和误差(按题目要求,此处未处理)'
def GSiterate(A, B, X0, e):
    B = B.T
    X_k = X0
    'shape (行，列)形式的元组'
    X_k1 = zeros(X0.shape)
    n = B.shape[0] #取行数
    delta = 10 #为当前精度
    k = 0 #循环次数
    k_max = 500 #最大循环次数
    while delta > e:
        '外层为迭代'
        for i in range(n):
            '内层为更新每行所有的值'
            # print i, B[i], A[i,0:i], X_k1[0:i], A[i,i:n], X_k[i:n], A[i,i]
            # print dot(A[i,0:i],X_k1[0:i])
            'A[i,0:i] 与 X_k1[0:i] 都是一维的行/列向量，所以dot()[0]也可以写成dot()'
            X_k1[i] = X_k[i] + 1.0 * ( B[i] - dot(A[i,0:i],X_k1[0:i])[0] - dot(A[i,i:n], X_k[i:n])[0] ) / A[i,i]

        delta = max(abs(X_k1-X_k))
        X_k = X_k1.copy()
        result = X_k.T[0]
        k = k + 1
        if k > k_max:
            print u"迭代次数：%s" % k
            return result,delta
    print u"迭代次数：%s" % k
    return result,delta

'A B 为线性方程组， x0为初值，e为精度'
def Jiterate(A, B, X0, e):
    B = B.T
    X_k = X0
    'shape (行，列)形式的元组'
    X_k1 = zeros(X0.shape)
    n = B.shape[0] #取行数
    delta = 10 #为当前精度
    k = 0 #循环次数
    k_max = 500 #最大循环次数
    while delta > e:
        '外层为迭代'
        for i in range(n):
            '内层为更新每行所有的值'
            # print i, B[i], A[i,0:i], X_k1[0:i], A[i,i:n], X_k[i:n], A[i,i]
            # print dot(A[i,0:i],X_k1[0:i])
            'A[i,0:i] 与 X_k1[0:i] 都是一维的行/列向量，所以dot()[0]也可以写成dot()'
            X_k1[i] = 1.0 * ( B[i] - dot(A[i,0:i],X_k[0:i])[0] - dot(A[i,i+1:n], X_k[i+1:n])[0] ) / A[i,i]
            # print i,X_k1[i]
            # print

        delta = max(abs(X_k1-X_k))
        X_k = X_k1.copy()
        result = X_k.T[0]
        k = k + 1
        if k > k_max:
            print u"迭代次数：%s" % k
            return result,delta
    print u"迭代次数：%s" % k
    return result,delta

'A B 为线性方程组， x0为初值，e为精度 w为松弛因子'
def SORiterate(A, B, X0, e, w):
    B = B.T
    X_k = X0
    'shape (行，列)形式的元组'
    X_k1 = zeros(X0.shape)
    n = B.shape[0] #取行数
    delta = 10 #为当前精度
    k = 0 #循环次数
    k_max = 500 #最大循环次数
    while delta > e:
        '外层为迭代'
        for i in range(n):
            '内层为更新每行所有的值'
            # print i, B[i], A[i,0:i], X_k1[0:i], A[i,i:n], X_k[i:n], A[i,i]
            # print dot(A[i,0:i],X_k1[0:i])
            'A[i,0:i] 与 X_k1[0:i] 都是一维的行/列向量，所以dot()[0]也可以写成dot()'
            X_k1[i] = X_k[i] + w * ( B[i] - dot(A[i,0:i],X_k1[0:i])[0] - dot(A[i,i:n], X_k[i:n])[0] ) / A[i,i]
            # print i,X_k1[i]
            # print

        delta = max(abs(X_k1-X_k))
        X_k = X_k1.copy()
        result = X_k.T[0]
        k = k + 1
        if k > k_max:
            print u"迭代次数：%s" % k
            return result,delta
    print u"迭代次数：%s" % k
    return result, delta

if __name__ == '__main__':
    a = A2
    b = B2
    print b.shape[0]
    X0 = array([[(i/i)-1 for i in xrange(1,b.shape[0]+1)]])
    X0 = matrix(X0)
    X0 = X0.getT()
    print "X0: "
    print X0
    e = 1e-3


    print "J: "
    X1,eX1 = Jiterate(a, b, X0, e)
    print X1
    print eX1
    print "\n\n"
    print "GS: "
    X2 = GSiterate(a, b, X0, e)
    print X2
    print "\n\n"
    print "SOR: "
    w = [i/10.0 for i in xrange(8,13)]
    for i in w:
        print "in w=%s" % i
        X3 = SORiterate(a, b, X0, e, i)
        print X3
        print
    
    # 使用numpy包中的linalg.solve()方法解多元一次方程
    X = linalg.solve(a,b)
    print X

# (array([  8.07747219e+05,  -1.32452450e+06,   1.07765341e+07,
#         -2.23974294e+07,  -2.91271361e+07,   1.53590948e+07,
#         -2.14435677e+07,   1.09841072e+08,   2.01860617e+06,
#          3.65457976e+08]), array([  3.44091506e+08]))
# [  1.00000000e+00  -1.00000000e+00   8.26924736e-15   1.00000000e+00
#    2.00000000e+00   1.36748025e-16   3.00000000e+00   1.00000000e+00
#   -1.00000000e+00   2.00000000e+00]