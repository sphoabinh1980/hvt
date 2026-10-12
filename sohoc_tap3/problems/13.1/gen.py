import random
def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%d %d %d\n' % x for x in qs)
def samples():
    return [(fmt([(10, 3, 0), (10, 3, 1), (7, 3, 2)]), '66\n36\n3\n'), (fmt([(5, 7, 1), (0, 4, 0), (10**6, 10**6, 1), (10**6, 10**6, 10**6)]), '0\n1\n1\n0\n')]
def tests():
    r = random.Random(131)
    T = {1: [fmt([(r.randint(0, 10), r.randint(1, 5), r.randint(0, 4)) for _ in range(100)])],
         2: [fmt([(r.randint(0, 2000), r.randint(1, 2000), r.randint(0, 3)) for _ in range(10**5)]), fmt([(2000, 2000, 0)] * 10 + [(2000, r.randint(1, 2000), 0) for _ in range(10**5 - 10)])],
         3: [fmt([(r.randint(0, 10**6), r.randint(1, 10**6), r.choice([0, 0, 1, r.randint(0, 10**6)])) for _ in range(10**5)]),
             fmt([(10**6, 10**6, 0)] * 50000 + [(10**6, r.randint(1, 10**6), 0) for _ in range(50000)]),
             fmt([(10**6, 10**6, 10**6), (10**6, 1, 10**6), (10**6, 1000, 1000), (0, 1, 0), (10**6, 999999, 1)] * 20000)]}
    return T
def small(r):
    return fmt([(r.randint(0, 30), r.randint(1, 8), r.randint(0, 5)) for _ in range(20)])
