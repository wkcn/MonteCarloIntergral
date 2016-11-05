#coding=utf-8
import random
import time
import math

tick_time = time.time()
def tick(t = True):
    global tick_time
    if t:
        print "Use Time: ", time.time() - tick_time
    tick_time = time.time()

def weiyuan(f, a, b, n):
    w = len(a)
    d = [(b[i] - a[i]) * 1.0 / n for i in range(w)]
    dd = 1.0
    for q in d:
        dd *= q
    x = [0.0 for _ in range(w)]
    s = [0.0]
    def go(k, s):
        if (k == w):
            s[0] += f(x) * dd
            return
        for i in range(n):
            x[k] = a[k] + d[k] * i
            go(k + 1,s)
    go(0,s)
    return s[0]

def mcup(f,a,b,n):
    w = len(a)
    d = [(b[i] - a[i]) for i in range(w)]
    dd = 1.0
    for q in d:
        dd *= q
    rec = [None for _ in range(n)]
    L = float("inf")
    H = float("-inf")
    for i in range(n):
        x = [random.random() * d[k] + a[k] for k in range(w)]
        y = f(x)
        if y < L:
            L = y
        if y > H:
            H = y
        rec[i] = y
    r = 0
    for y in rec:
        if random.random() * (H-L) <= (y - L):
            r += 1
    return dd * (H - L) * 1.0 * r / n + L * dd
