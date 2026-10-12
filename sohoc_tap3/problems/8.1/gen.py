import random
def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%d %d\n' % x for x in qs)
def seg(r, lo, hi, w):
    L = r.randint(lo, hi - w); return (L, L + w)
def samples():
    return [(fmt([(1, 10), (100, 130), (24, 28)]), '4 17\n6 660\n0 0\n'),
            (fmt([(999999999900, 10**12), (999966000289, 999966000289), (1, 1)]), '4 3999999999846\n0 0\n0 0\n')]
def tests():
    r = random.Random(81)
    T = {1: [fmt([seg(r, 1, 10**7, 10**6) for _ in range(10)]), fmt([(1, 10**6), (9 * 10**6, 10**7), (1, 1), (2, 2), (1, 2)] * 2), fmt([seg(r, 1, 10**7, r.randint(0, 10**6)) for _ in range(10)])],
         2: [fmt([seg(r, 1, 10**12, 100) for _ in range(10)]), fmt([(10**12 - 100, 10**12), (999966000289 - 50, 999966000289 + 50), (1, 100), (999999999989, 999999999989)] * 2 + [(2, 2), (1, 1)])],
         3: [fmt([seg(r, 1, 10**12, 10**6) for _ in range(10)]), fmt([(10**12 - 10**6, 10**12)] * 10), fmt([(1, 10**6), (999999000000, 10**12), (999966000289 - 500000, 999966000289 + 500000)] * 3 + [(10**12, 10**12)])]}
    return T
def small(r):
    return fmt([seg(r, 1, r.choice([1000, 10**12]), r.randint(0, 200)) for _ in range(5)])
