import random, math
def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%d %d %d %d %d\n' % x for x in qs)
def rq(r, A, M, X, cop=False, Q=10):
    out = []
    while len(out) < Q:
        m = r.randint(1, M)
        a = r.randint(-A, A)
        if cop and math.gcd(a, m) != 1: continue
        if r.random() < 0.4 and not cop:
            g = math.gcd(a, m); c = g * r.randint(-A // max(g, 1), A // max(g, 1))
        else:
            c = r.randint(-A, A)
        L = r.randint(-X, X); R = r.randint(L, X)
        out.append((a, c, m, L, R))
    return out
def samples():
    return [(fmt([(6, 4, 10, 0, 20), (6, 3, 10, 0, 100), (3, 2, 5, -10, 10)]), '4 4\n0\n4 -6\n'),
            (fmt([(0, 0, 7, -5, 5), (0, 3, 7, -5, 5), (-3, 1, 10**18, -10**18, 0)]), '11 -5\n0\n1 -666666666666666667\n')]
def tests():
    r = random.Random(103)
    T = {1: [fmt(rq(r, 10**18, 10**6, 10**6)) for _ in range(3)] + [fmt(rq(r, 1000, 1000, 10**6)), fmt([(0, 0, 1, -10**6, 10**6), (0, 5, 10**6, -10**6, 10**6), (10**6, 0, 10**6, -10**6, 10**6), (2, 1, 4, -10**6, 10**6), (-7, -3, 999983, -10**6, 10**6)] * 2)],
         2: [fmt(rq(r, 10**18, 10**9, 10**18, True, 10**5)), fmt(rq(r, 10**9, 10**9, 10**18, True, 10**5))],
         3: [fmt(rq(r, 10**18, 10**18, 10**18, False, 10**5)), fmt(rq(r, 10**18, 10**18, 10**18, True, 10**5)),
             fmt([(0, 0, r.randint(1, 10**18), -10**18, 10**18) for _ in range(5)] + [(-3, 1, 10**18, -10**18, 0)] * 5 + rq(r, 10**18, 10**18, 10**18, False, 99990))]}
    return T
def small(r):
    return fmt(rq(r, 50, 30, 60, False, 10))
