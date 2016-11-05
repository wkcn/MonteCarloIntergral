#coding=utf-8
from math import *
from lib2 import *
f = lambda x:x[0] ** 2 + x[1] ** 3 + cos(x[2])
a = [0,-3,-10]
b = [10,8,10]

tick(False)
print weiyuan(f,a,b,100)
tick()
print mcup(f,a,b,100000);
tick()
