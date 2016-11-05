#coding=utf-8
from math import *
from lib import *
# 函数
f = lambda x:cos(x) + x ** 3
# 下界
a = 1
# 上界
b = 10


tick(False)
print weiyuan(f,a,b,10000)
tick()
print mcup2(f,a,b,err=100,p = 0.2)
tick()
