import random
def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%d %d\n' % x for x in qs)
def rq(r, lim, Q, short=False):
    out = []
    for _ in range(Q):
        if short:
            a = r.randint(1, lim); b = min(lim, a + r.randint(0, 30))
        else:
            a, b = sorted((r.randint(1, lim), r.randint(1, lim)))
        out.append((a, b))
    return out
def samples():
    return [(fmt([(1, 20), (5, 13), (6, 12), (3, 5)]), '4\n2\n0\n1\n'), (fmt([(1, 10**7), (9999000, 10**7), (4, 4)]), '58980\n4\n0\n')]
def tests():
    r = random.Random(62)
    T = {1: [fmt(rq(r, 10**4, 100)), fmt(rq(r, 10**4, 100, True)), fmt([(1, 10**4), (3, 5), (5, 7), (4, 6), (6, 12), (1, 1), (2, 3), (9999, 10**4), (11, 13), (12, 13)] * 10)],
         2: [fmt([(r.randint(1, 1000), 10**7 - r.randint(0, 1000)) for _ in range(100)]), fmt(rq(r, 10**7, 100)), fmt(rq(r, 10**7, 100, True))],
         3: [fmt(rq(r, 10**7, 10**6)), fmt([(r.randint(1, 100), 10**7 - r.randint(0, 100)) for _ in range(10**6)]), fmt(rq(r, 10**7, 10**6, True))]}
    return T
def small(r):
    return fmt(rq(r, 400, 30, r.random() < 0.5))
