import random
def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%d %d %d %d %d\n' % x for x in qs)
def rq(r, Q, lim, w=None, Rmax=10**18):
    out = []
    for _ in range(Q):
        if w is not None:
            L = r.randint(1, Rmax - w); R = L + r.randint(0, w)
        else:
            L, R = sorted((r.randint(1, Rmax), r.randint(1, Rmax)))
        g = r.randint(1, 20)
        abc = [r.choice([r.randint(1, lim), g * r.randint(1, max(1, lim // g)), r.randint(1, 30)]) for _ in range(3)]
        out.append((L, R, *abc))
    return out
def samples():
    return [(fmt([(1, 30, 2, 3, 5), (10, 20, 4, 6, 12)]), '16\n3\n'),
            (fmt([(1, 10**18, 1000000007, 1000000009, 998244353), (1, 10**18, 4, 6, 10**18)]), '1999999982\n333333333333333332\n')]
def tests():
    r = random.Random(141)
    T = {1: [fmt(rq(r, 10, 10**18, 10**5)), fmt(rq(r, 10, 100, 10**5)), fmt([(1, 100000, 2, 3, 5), (10**18 - 10**5, 10**18, 10**18, 1, 7), (1, 1, 1, 1, 1)] * 3)],
         2: [fmt(rq(r, 10**5, 10**6)), fmt(rq(r, 10**5, 1000))],
         3: [fmt(rq(r, 10**5, 10**18)), fmt(rq(r, 10**5, 10**9)), fmt([(1, 10**18, 1000000007, 1000000009, 998244353), (1, 10**18, 4, 6, 10**18), (1, 10**18, 10**18, 10**18 - 1, 10**18 - 2)] * 33333)]}
    return T
def small(r):
    return fmt(rq(r, 10, r.choice([10, 100, 10**18]), 300, 2000))
