import random
from math import comb
def g(n, k):
    if n < 0: return 0
    t = 0; s = 0
    for i in range(60, -1, -1):
        if n >> i & 1:
            if k - t >= 0: s += comb(i, k - t)
            t += 1
    return s + (1 if t == k else 0)
def t1(r, M):
    a, b = r.randint(0, M), r.randint(0, M); return '1 %d %d %d' % (min(a, b), max(a, b), r.choice([0, 1, 2, r.randint(0, 60), r.randint(1, 30)]))
def t2(r, M):
    while True:
        x = r.randint(1, M); k = bin(x).count('1')
        if k <= 59: break
    return '2 %d %d' % (k, g(x, k) - (1 if k == 0 else 0))
def fmt(qs): return '%d\n' % len(qs) + '\n'.join(qs) + '\n'
def samples():
    return [(fmt(['1 1 12 2', '2 2 4', '1 0 10 0']), '6\n9\n1\n'), (fmt(['1 1 1000000000000000000 30', '2 59 1']), '103477184498507572\n576460752303423487\n')]
def tests():
    r = random.Random(183)
    return {1: [fmt([t1(r, 10**5) if r.random() < 0.5 else t2(r, 10**5) for _ in range(10**5)]), fmt(['1 0 0 0', '1 0 100000 17', '2 1 16', '2 16 1'])],
            2: [fmt([t1(r, 10**18) for _ in range(10**5)]), fmt(['1 0 1000000000000000000 %d' % k for k in range(61)])],
            3: [fmt([t1(r, 10**18) if r.random() < 0.5 else t2(r, 10**18) for _ in range(10**5)]), fmt(['2 59 1', '2 1 59', '2 30 %d' % g(10**18, 30), '2 2 1'])]}
def small(r):
    return fmt([t1(r, 3000) if r.random() < 0.5 else t2(r, 3000) for _ in range(20)])
