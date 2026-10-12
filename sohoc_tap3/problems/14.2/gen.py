import random
from sympy import prevprime
def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%d %d\n' % x for x in qs)
def hard(r):
    t = r.random()
    if t < 0.4: return prevprime(r.randint(10**11, 10**12))
    if t < 0.6: return 200560490130
    if t < 0.8: return prevprime(r.randint(10**5, 10**6)) * prevprime(r.randint(10**5, 10**6))
    return r.randint(1, 10**12)
def samples():
    return [(fmt([(30, 100), (12, 12), (1, 5)]), '26\n4\n5\n'), (fmt([(999999999989, 10**12), (200560490130, 10**12)]), '999999999999\n152852151382\n')]
def tests():
    r = random.Random(142)
    T = {1: [fmt([(r.randint(1, 10**12), r.randint(1, 10**6)) for _ in range(10)]), fmt([(200560490130, 10**6), (1, 10**6), (999999999989, 10**6), (2, 1), (10**12, 10**6)] * 2)],
         2: [fmt([(hard(r), r.randint(1, 10**12)) for _ in range(10)]), fmt([(999999999989, 10**12)] * 10)],
         3: [fmt([(hard(r), r.randint(1, 10**12)) for _ in range(1000)]), fmt([(prevprime(r.randint(10**11, 10**12)), 10**12) for _ in range(1000)]),
             fmt([(7420738134810 // 37, r.randint(1, 10**12)) for _ in range(1000)])]}
    return T
def small(r):
    return fmt([(r.randint(1, 3000), r.randint(1, 3000)) for _ in range(20)])
