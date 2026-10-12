import random
def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%d %d %d\n' % x for x in qs)
def samples():
    return [(fmt([(3, 5, 30), (6, 4, 7), (3, 5, 7)]), '3\n0\n0\n'),
            (fmt([(1, 1, 10**18), (10**9, 10**9, 10**18), (2, 3, 0)]), '1000000000000000001\n1000000001\n1\n')]
def tests():
    r = random.Random(42)
    T = {1: [], 2: [], 3: []}
    T[1].append(fmt([(r.randint(1, 10**9), r.randint(1, 10**9), r.randint(0, 10**7)) for _ in range(10)]))
    T[1].append(fmt([(1, 1, 10**7), (1, 2, 10**7), (3, 5, 10**7), (999983, 999979, 10**7), (6, 4, 9999999), (2, 2, 10**7), (7, 7, 0), (1, 10**9, 10**7), (10**9, 1, 10**7), (12, 18, 9999990)]))
    T[2].append(fmt([(r.randint(1, 10**6), r.randint(1, 10**6), r.randint(0, 10**18)) for _ in range(10)]))
    T[2].append(fmt([(999983, 999979, 10**18), (1, 1, 10**18), (10**6, 10**6, 10**18), (999999, 999998, 999997000002), (2, 4, 10**18 - 1), (1, 10**6, 10**18), (3, 7, 11), (500000, 999999, 10**18 - 7), (6, 10, 10**18), (999983, 1, 0)]))
    T[3].append(fmt([(r.randint(1, 10**9), r.randint(1, 10**9), r.randint(0, 10**18)) for _ in range(10**5)]))
    T[3].append(fmt([(r.choice([1, 2, 999999937, 10**9]), r.choice([1, 3, 999999929, 10**9]), r.randint(0, 10**18)) for _ in range(10**5)]))
    T[3].append(fmt([(g * r.randint(1, 10**4), g * r.randint(1, 10**4), g * r.randint(0, 10**12)) for g in [r.randint(1, 10**5) for _ in range(10**5)]]))
    T[3].append(fmt([(999999937, 999999929, 10**18 - r.randint(0, 10**9)) for _ in range(10**5)]))
    return T
def small(r):
    return fmt([(r.randint(1, 30), r.randint(1, 30), r.randint(0, 300)) for _ in range(10)])
