import random
import time
import math

tick_time = time.time()
def tick(t = True):
    global tick_time
    if t:
        print "Use Time: ", time.time() - tick_time
    tick_time = time.time()

def weiyuan(f, a, b, n = 10000):
    d = (b - a) * 1.0 / n
    x = a
    res = 0.0
    for i in range(n):
        res += f(x) * d
        x += d
    return res

def mc(f,a,b,L,H,n):
    r = 0
    for i in range(n):
        x = random.random() * (b - a) + a
        y = f(x)
        if random.random() <= (y - L) * 1.0 / (H-L): 
            r += 1
    return (b - a) * (H - L) * 1.0 * r / n + L * (b - a)

def mcup(f,a,b,n):
    rec = [None for _ in range(n)]
    L = float("inf")
    H = float("-inf")
    for i in range(n):
        x = random.random() * (b - a) + a
        y = f(x)
        if y < L:
            L = y
        if y > H:
            H = y
        rec[i] = y
    print "Low: %lf, High: %lf" % (L, H)
    r = 0
    for y in rec:
        if random.random() * (H-L) <= (y - L):
            r += 1
    return (b - a) * (H - L) * 1.0 * r / n + L * (b - a)


def mcup_in(f,a,b,L,H,rec,n):
    for i in range(n):
        x = random.random() * (b - a) + a
        y = f(x)
        if y < L:
            L = y
        if y > H:
            H = y
        rec.append(y)
    return L, H

def mcup2(f,a,b,err,p):
    rec = []
    L = float("inf")
    H = float("-inf")
    sample = 100
    n = 0
    r = 0
    while 1:
        L_new,H_new = mcup_in(f,a,b,L,H,rec,sample)
        L = L_new
        H = H_new
        n += sample
        r = 0
        for y in rec:
            if random.random() * (H-L) <= (y - L):
                r += 1
        res_new = (b - a) * (H - L) * 1.0 * r / n + L * (b - a)

        u = (((b - a) ** 2) * (H - L) ** 2  * 1.0 )/ (4.0 * (err ** 2) * p) 
        if n > u:
            break
    return res_new
