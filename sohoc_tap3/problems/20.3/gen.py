import random
def F(T): return '%d\n' % len(T) + ''.join('%d %d\n%d %d\n%d %d\n' % t for t in T)
def tri(r, M):
    while True:
        t = tuple(r.randint(-M, M) for _ in range(6))
        x1, y1, x2, y2, x3, y3 = t
        if (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) != 0: return t
E = 10**18
def samples():
    return [(F([(0, 0, 4, 0, 0, 4), (1, 1, 13, 9, 13, 2)]), '3\n37\n'),
            (F([(0, 0, E, 0, 0, E), (0, 0, E, E, E, E - 1)]), '499999999999999998500000000000000001\n0\n')]
def tests():
    r = random.Random(203)
    B = 10**9
    return {1: [F([tri(r, 100) for _ in range(10**5)]), F([(-100, -100, 100, -100, -100, 100), (-100, -100, 100, 100, 100, 99)])],
            2: [F([tri(r, B) for _ in range(10**5)]), F([(-B, -B, B, -B, -B, B), (-B, -B, B, B, B, B - 1), (-B, B, B, -B, B, B)])],
            3: [F([tri(r, E) for _ in range(10**5)]), F([(-E, -E, E, -E, -E, E), (-E, -E, E, E, E, E - 1), (-E, E, E, -E, E, E), (0, 0, E, 0, 0, E)]),
                F([tri(r, 10**12) for _ in range(10**5)])]}
def small(r):
    return F([tri(r, 12) for _ in range(10)])
