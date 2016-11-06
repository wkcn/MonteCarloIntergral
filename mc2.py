#coding=utf-8
from math import *
from lib2 import *
'''
f = lambda x:x[0] ** 2 + x[1] ** 3 + cos(x[2])
a = [0,-3,-10]
b = [10,8,10]
'''
f = lambda x : x[0] * x[1] + x[2] * 1.0 / x[3] 
a = [1,-9,3,1]
b = [3,5,4,10]

tick(False)
print mcup(f,a,b,500000);
tick()
print weiyuan(f,a,b,int(1000000 **  (1.0 / len(a))) + 1)
tick()
