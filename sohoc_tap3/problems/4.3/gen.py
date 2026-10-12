import random
def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%d %d %d %d %d %d\n' % x for x in qs)
def rq(r, mmax, Tmax, Q):
    out = []
    for _ in range(Q):
        m = r.randint(1, mmax)
        if r.random() < 0.3:
            g = r.randint(1, 50); m = max(g, m - m % g)
            a, b = r.randrange(m), r.randrange(m)
            a = (b + g * r.randrange(max(1, m // g))) % m
        else:
            a, b = r.randrange(m), r.randrange(m)
        p, q = r.randrange(m), r.randrange(m)
        if r.random() < 0.1: a = b
        if r.random() < 0.05: q = p
        out.append((m, p, a, q, b, r.randint(0, Tmax)))
    return out
def samples():
    return [(fmt([(12, 0, 5, 3, 2, 10), (12, 0, 4, 1, 0, 100), (60, 7, 13, 7, 13, 5)]), '1 3\n-1 0\n0 6\n'),
            (fmt([(10**18, 0, 3, 1, 0, 10**18), (1, 0, 0, 0, 0, 10**18)]), '666666666666666667 1\n0 1000000000000000001\n')]
def tests():
    r = random.Random(43)
    T = {1: [fmt(rq(r, 1000, 10**6, 10)) for _ in range(4)] + [fmt([(1000, 0, 999, 0, 0, 10**6), (997, 5, 3, 7, 3, 10**6), (1, 0, 0, 0, 0, 10**6), (1000, 1, 500, 0, 0, 10**6), (999, 0, 1, 998, 0, 0), (12, 0, 5, 3, 2, 10), (1000, 999, 1, 0, 0, 0), (2, 0, 1, 1, 0, 10**6), (1000, 3, 7, 3, 7, 10**6), (640, 1, 32, 33, 0, 999999)])],
         2: [fmt(rq(r, 10**9, 10**18, 10**5)) for _ in range(3)] + [fmt([(999999937, 0, 1, 999999936, 0, 10**18)] * 10**5)],
         3: [fmt(rq(r, 10**18, 10**18, 10**5)) for _ in range(3)] + [fmt([(10**18, 0, 3, 1, 0, 10**18), (999999999999999989, 0, 999999999999999988, 5, 0, 10**18), (2**60, 1, 2**59 + 1, 0, 1, 10**18), (10**18, 7, 5 * 10**17, 7, 0, 10**18)] * 25000)]}
    return T
def small(r):
    return fmt(rq(r, 40, 120, 10))
