import random
M = 10**9 + 7
def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%d %d\n' % x for x in qs)
def samples():
    return [(fmt([(2, 10), (3, 10**18), (M, 5)]), '1024\n246336683\n0\n'), (fmt([(0, 0), (M, 0), (10**18, 10**18)]), '1\n1\n504853526\n')]
def tests():
    r = random.Random(91)
    T = {1: [fmt([(r.randint(0, 10**18), r.randint(0, 10**6)) for _ in range(10)]), fmt([(0, 0), (0, 10**6), (1, 10**6), (M, 0), (2, 10**6), (M - 1, 999999), (10**18, 10**6), (M + 1, 10**6), (2 * M, 3), (10**18, 0)])],
         2: [fmt([(r.randint(0, M - 1), r.randint(0, 10**18)) for _ in range(10**5)]), fmt([(M - 1, 10**18 - r.randint(0, 5)) for _ in range(10**5)])],
         3: [fmt([(r.randint(0, 10**18), r.randint(0, 10**18)) for _ in range(10**5)]), fmt([(10**18 - r.randint(0, 10**6), 10**18) for _ in range(10**5)]), fmt([(k * M, r.randint(0, 3)) for k in range(1, 10**5 + 1)])]}
    return T
def small(r):
    return fmt([(r.choice([r.randint(0, 50), r.randint(0, 10**18), M * r.randint(0, 3)]), r.randint(0, 2000)) for _ in range(10)])
