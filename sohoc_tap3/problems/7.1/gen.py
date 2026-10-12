import random
def fmt(xs):
    return '%d\n' % len(xs) + ''.join('%d\n' % x for x in xs)
def samples():
    return [(fmt([1, 12, 360, 97]), '1 1\n6 28\n24 1170\n2 98\n'), (fmt([10**7, 8648640, 9999991]), '64 24902280\n448 40965120\n2 9999992\n')]
def tests():
    r = random.Random(71)
    T = {1: [fmt([r.randint(1, 10**4) for _ in range(1000)]), fmt([1, 2, 9973, 10**4, 5040, 7560, 8190, 9240, 4096, 6561] * 100)],
         2: [fmt([r.randint(1, 10**7) for _ in range(1000)]), fmt([9999991, 9979200, 8648640, 10**7, 9999973] * 200)],
         3: [fmt([r.randint(1, 10**7) for _ in range(10**6)]), fmt([9999991] * 500000 + [9979200] * 500000), fmt([r.randint(10**7 - 1000, 10**7) for _ in range(10**6)])]}
    return T
def small(r):
    return fmt([r.randint(1, 3000) for _ in range(30)])
