import random
def fmt(xs):
    return '%d\n' % len(xs) + ''.join('%d\n' % x for x in xs)
def samples():
    return [(fmt([4, 10, 98, 9, 11]), '2 2\n3 7\n19 79\n2 7\n-1\n'),
            (fmt([2, 999999634148, 10**12, 999999999991]), '-1\n1669 999999632479\n11 999999999989\n2 999999999989\n')]
def tests():
    r = random.Random(52)
    ev = lambda lo, hi: 2 * r.randint(lo // 2, hi // 2)
    T = {1: [fmt([ev(4, 10**6) for _ in range(100)]), fmt([10**6, 999998, 4, 6, 8, 98, 128, 999994] * 12 + [2] * 4), fmt([ev(900000, 10**6) for _ in range(100)])],
         2: [fmt([ev(10**11, 10**12) for _ in range(100)]), fmt([999999634148] * 50 + [10**12] * 50), fmt([ev(10**12 - 2 * 10**6, 10**12) for _ in range(100)])],
         3: [fmt([r.randint(2, 10**12) for _ in range(100)]), fmt([2 * r.randint(10**10, 5 * 10**11) + 1 for _ in range(100)]),
             fmt([999999999991, 999999999989 + 2, 999999999999, 3, 5, 7, 9, 999999999961 + 2, 999966000289 + 2, 2] * 10),
             fmt([999999634148] * 50 + [ev(10**12 - 10**6, 10**12) + 1 for _ in range(50)])]}
    return T
def small(r):
    return fmt([r.randint(2, 3000) for _ in range(20)])
