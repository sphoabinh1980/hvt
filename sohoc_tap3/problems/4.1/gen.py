import random
def fmt(a, c):
    return '%d %d\n%s\n%s\n' % (len(a), len(c), ' '.join(map(str, a)), ' '.join(map(str, c)))
def cs(r, g, Q, lim):
    return [r.choice([0, g * r.randint(0, lim // g), r.randint(0, lim)]) for _ in range(Q)]
def samples():
    return [(fmt([6, 4], [7, 2, 10]), '2\nKHONG\nCO\nCO\n'), (fmt([6, 10, 15], [1, 0, 10**18]), '1\nCO\nCO\nCO\n')]
def tests():
    r = random.Random(41)
    T = {1: [], 2: [], 3: []}
    for a in [(6, 4), (1000, 999), (12, 18), (7, 7), (1, 1000), (r.randint(1, 1000), r.randint(1, 1000))]:
        from math import gcd
        T[1].append(fmt(list(a), cs(r, gcd(*a), 1000 if a != (1, 1000) else 100000, 1000)))
    from math import gcd
    for _ in range(4):
        g = r.randint(1, 10**9)
        a = [g * r.randint(1, 10**9), g * r.randint(1, 10**9)]
        T[2].append(fmt(a, cs(r, gcd(*a), 10**5, 10**18)))
    T[2].append(fmt([10**18, 10**18 - 1], cs(r, 1, 10**5, 10**18)))
    for k in range(4):
        base = [2 * 3 * 5 * 7, 2 * 3 * 11 * 13, 5 * 7 * 11 * 17, 3 * 13 * 17 * 19]
        g = r.randint(1, 1000)
        a = [g * base[i % 4] * r.randint(1, 10**9) for i in range(10**5)] if k < 2 else [g * r.choice(base) for _ in range(10**5)]
        gg = 0
        for x in a: gg = gcd(gg, x)
        T[3].append(fmt(a, cs(r, gg, 10**5, 10**18)))
    T[3].append(fmt([6, 10, 15] + [30] * 99997, cs(r, 1, 10**5, 10**18)))
    T[3].append(fmt([10**18] * 10**5, cs(r, 10**18, 10**5, 10**18)))
    return T
def small(r):
    n = r.randint(1, 4)
    g = r.randint(1, 6)
    a = [g * r.randint(1, 30) for _ in range(n)]
    return fmt(a, [r.randint(0, 200) for _ in range(20)])
