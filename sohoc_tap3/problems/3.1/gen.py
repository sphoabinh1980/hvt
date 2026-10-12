import random
def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%d %d\n' % x for x in qs)
def fib(k):
    a, b = 1, 1
    for _ in range(k): a, b = b, a + b
    return a, b
def samples():
    return [(fmt([(252, 105), (6, 4)]), '21 60\n2 6\n'),
            (fmt([(10**18, 999999), (999999999999999999, 3)]), '1 999999000000000000000000\n3 333333333333333333\n')]
def tests():
    r = random.Random(31)
    T = {1: [], 2: [], 3: []}
    T[1].append(fmt([(r.randint(1, 10**6), r.randint(1, 10**6)) for _ in range(10)]))
    T[1].append(fmt([(999983, 999979), (10**6, 10**6), (1, 1), (1, 10**6), (720720, 997920), (832040, 514229), (999999, 999998), (2, 4), (10**6, 1), (524288, 999424)]))
    T[2].append(fmt([(r.randint(1, 10**9), r.randint(1, 10**9)) for _ in range(10**5)]))
    T[2].append(fmt([(g * r.randint(1, 1000), g * r.randint(1, 1000)) for g in [r.randint(1, 10**6) for _ in range(10**5)]]))
    T[2].append(fmt([fib(43)[::-1] for _ in range(10**5)]))
    T[3].append(fmt([(r.randint(1, 10**18), r.randint(1, 10**18)) for _ in range(10**5)]))
    T[3].append(fmt([fib(86)[::-1]] * 50000 + [(10**18, 999999)] * 50000))
    T[3].append(fmt([(g * r.randint(1, 10**6), g * r.randint(1, 10**6)) for g in [r.randint(1, 10**12) for _ in range(10**5)]]))
    T[3].append(fmt([(10**18, 10**18), (10**18, 1), (1, 1), (999999999999999989, 999999999999999877)] * 25000))
    return T
def small(r):
    return fmt([(r.randint(1, 3000), r.randint(1, 3000)) for _ in range(10)])
