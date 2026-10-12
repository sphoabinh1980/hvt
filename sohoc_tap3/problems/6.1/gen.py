import random
def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%d %d\n' % x for x in qs)
def samples():
    return [(fmt([(1, 10), (1, 100), (2, 1), (2, 25), (1, 1), (1, 2)]), '4\n25\n2\n97\n0\n1\n'),
            (fmt([(1, 10**7), (2, 664579), (2, 100000), (1, 9999990)]), '664579\n9999991\n1299709\n664578\n')]
def tests():
    r = random.Random(61)
    T = {1: [fmt([(t, r.randint(1, 10**4) if t == 1 else r.randint(1, 1000)) for t in [r.randint(1, 2) for _ in range(100)]]),
             fmt([(1, 10**4), (2, 1000), (1, 1), (2, 1), (1, 2), (1, 3), (2, 2), (1, 9973), (1, 9972), (2, 999)] * 10)],
         2: [fmt([(1, r.randint(1, 10**7)) for _ in range(10**6)]), fmt([(1, 10**7 - r.randint(0, 100)) for _ in range(10**6)])],
         3: [fmt([(t, r.randint(1, 10**7) if t == 1 else r.randint(1, 664579)) for t in [r.randint(1, 2) for _ in range(10**6)]]),
             fmt([(2, 664579 - r.randint(0, 1000)) for _ in range(10**6)]), fmt([(2, 1), (1, 1)] * 500000)]}
    for k in (1, 2):
        pass
    return {1: T[1], 2: T[2], 3: T[3]}
def small(r):
    return fmt([(t, r.randint(1, 300) if t == 1 else r.randint(1, 60)) for t in [r.randint(1, 2) for _ in range(30)]])
