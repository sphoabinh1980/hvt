import random
def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%d %d\n' % x for x in qs)
def rq(r, lim, Q):
    return [tuple(sorted((r.randint(1, lim), r.randint(1, lim)))) for _ in range(Q)]
def samples():
    return [(fmt([(1, 8), (2, 2), (5, 5)]), '21\n1\n4\n'), (fmt([(1, 1), (1, 10**7)]), '0\n30396356427241\n')]
def tests():
    r = random.Random(112)
    return {1: [fmt(rq(r, 1000, 10)), fmt([(1, 1000), (1, 1), (1, 2), (999, 1000), (500, 500), (2, 1000), (1000, 1000), (7, 7), (1, 3), (997, 997)])],
            2: [fmt(rq(r, 10**5, 10**5)), fmt([(1, 10**5)] * 10**5)],
            3: [fmt(rq(r, 10**7, 10**5)), fmt([(1, 10**7), (10**7, 10**7), (1, 1)] * 33333), fmt([(r.randint(1, 10), 10**7 - r.randint(0, 10)) for _ in range(10**5)])]}
def small(r):
    return fmt(rq(r, 200, 10))
