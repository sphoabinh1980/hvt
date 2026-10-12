import random
from sympy import primerange, prevprime
PR = list(primerange(2, 100001))
def fmt(m, qs):
    return '%d %d\n' % (len(qs), m) + ''.join('%d %d\n' % x for x in qs)
def sqfree(r, lim):
    while True:
        k = r.randint(1, 6); ps = r.sample(PR, k); m = 1
        for p in ps: m *= p
        if m <= lim: return m
def rq(r, N, Q):
    out = []
    for _ in range(Q):
        n = r.randint(0, N); k = r.choice([r.randint(0, n), r.randint(0, N), n, 0, 1])
        out.append((n, k))
    return out
def samples():
    return [(fmt(7, [(1000, 500), (10, 3), (5, 7)]), '4\n1\n0\n'), (fmt(30, [(6, 3), (10, 5), (10**18, 1)]), '20\n12\n10\n')]
def tests():
    r = random.Random(133)
    T = {1: [fmt(sqfree(r, 10**10), rq(r, 2000, 10**5)), fmt(1, rq(r, 2000, 1000)), fmt(30, rq(r, 2000, 10**5)), fmt(9998000099, rq(r, 2000, 10**5))],
         2: [fmt(p, rq(r, 10**18, 10**5)) for p in [2, 3, 99991, 7, r.choice(PR)]],
         3: [fmt(sqfree(r, 10**10), rq(r, 10**18, 10**5)) for _ in range(3)] + [fmt(2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29, rq(r, 10**18, 10**5)), fmt(9998000099, rq(r, 10**18, 10**5)), fmt(1, rq(r, 10**18, 10**4))]}
    return T
def small(r):
    m = r.choice([1, 2, 6, 30, 7, 210, 99991, 9998000099, sqfree(r, 10**10)])
    return fmt(m, rq(r, 300, 20))
