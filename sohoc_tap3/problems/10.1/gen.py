import random
def fmt(b):
    return '%d\n' % len(b) + ''.join('%d %d\n' % x for x in b)
def bag(r, lim):
    s = r.randint(1, lim); x = r.choice([0, s, r.randint(0, s)]); return (x, s - x)
def samples():
    return [(fmt([(1, 1), (1, 2)]), '166666668\n666666672\n'), (fmt([(0, 5), (3, 0)]), '0\n1\n'), (fmt([(1, 999999999)] * 3), '793002921\n17492711\n')]
def tests():
    r = random.Random(101)
    T = {1: [fmt([bag(r, 10) for _ in range(r.randint(1, 10))]) for _ in range(6)],
         2: [fmt([bag(r, 10**9)]) for _ in range(6)] + [fmt([(10**9, 0)]), fmt([(0, 10**9)]), fmt([(1, 999999999)])],
         3: [fmt([bag(r, 10**9) for _ in range(10**5)]), fmt([(r.randint(1, 10), r.randint(1, 10)) for _ in range(10**5)]), fmt([(1, 999999999)] * 10**5),
             fmt([(r.randint(0, 3), r.randint(10**8, 10**9 - 3)) for _ in range(10**5)])]}
    return T
def small(r):
    return fmt([bag(r, r.choice([10, 10**9])) for _ in range(r.randint(1, 8))])
