import random
def fmt(q): return '%d\n' % len(q) + ''.join('%d\n' % x for x in q)
def samples():
    return [(fmt([11, 2026, 10**18]), '0\n7\n3\n')]
def tests():
    r = random.Random(4)
    return {1: [fmt([r.randint(1, 10**6) for _ in range(10)]), fmt([1, 9, 10, 189, 190, 10**6])],
            2: [fmt([r.randint(1, 10**18) for _ in range(10**5)]), fmt([10**18, 10**18 - 1, 9, 10, 189, 190, 2889, 2890] * 1000)]}
def small(r):
    return fmt([r.randint(1, 50000) for _ in range(30)])
