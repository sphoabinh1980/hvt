import random
def fmt(q): return '%d\n' % len(q) + ''.join('%d\n' % x for x in q)
def samples():
    return [(fmt([10, 15, 2026]), '2 8\n3 8\n505 2\n')]
def tests():
    r = random.Random(3)
    return {1: [fmt([r.randint(1, 10**5) for _ in range(10)]), fmt([1, 4, 5, 15, 25, 100000])],
            2: [fmt([r.randint(1, 10**18) for _ in range(10**5)]), fmt([10**18, 5**25, 5**25 - 1, 2**59] * 100)]}
def small(r):
    return fmt([r.randint(0, 3000) for _ in range(20)])
