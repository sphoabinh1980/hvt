import random
def fmt(xs):
    return '%d\n' % len(xs) + ''.join('%d\n' % x for x in xs)
def samples():
    return [(fmt([1, 10, 12, 26, 97]), '2\n11\n11\n23\n97\n'),
            (fmt([999999549106, 10**12, 999999999989]), '999999548953\n999999999989\n999999999989\n')]
def tests():
    r = random.Random(51)
    T = {1: [fmt(list(range(1, 101))), fmt([r.randint(1, 1000) for _ in range(100)]), fmt([1000, 997, 998, 999, 1, 2, 3, 4, 888, 908] * 10)],
         2: [fmt([r.randint(10**8, 10**9) for _ in range(100)]), fmt([999999937, 10**9, 999999929 + 4, 436273009 + 140] * 25),
             fmt([10**9 - r.randint(0, 1000) for _ in range(100)])],
         3: [fmt([r.randint(10**11, 10**12) for _ in range(100)]), fmt([999999549106] * 50 + [10**12] * 50),
             fmt([999999999989 - r.randint(0, 10**6) for _ in range(100)]), fmt([999999999989] * 100)]}
    return T
def small(r):
    return fmt([r.randint(1, 5000) for _ in range(20)])
