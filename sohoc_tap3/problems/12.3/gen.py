import random, math
def fmt(ms, qs):
    return '%d %d\n%s\n' % (len(ms), len(qs), ' '.join(map(str, ms))) + ''.join(' '.join(map(str, cs + [L, R])) + '\n' for cs, L, R in qs)
def rq(r, ms, Q, Rmax, good=0.7):
    out = []
    for _ in range(Q):
        if r.random() < good:
            x = r.randint(0, min(Rmax, 10**18)); cs = [x % m for m in ms]
        else:
            cs = [r.randrange(m) for m in ms]
        L = r.randint(0, Rmax); R = r.randint(L, Rmax)
        if r.random() < 0.3: L = 0; R = Rmax
        out.append((cs, L, R))
    return out
def samples():
    return [(fmt([10, 12], [([2, 6], 0, 1000), ([0, 1], 0, 1000), ([0, 0], 17, 100)]), '60\n16 42\n0\n1 60\n'),
            (fmt([4, 6, 9], [([1, 3, 3], 0, 100), ([1, 2, 0], 0, 100), ([3, 5, 8], 0, 10**18)]), '36\n3 21\n0\n27777777777777777 35\n')]
def tests():
    r = random.Random(123)
    T = {1: [], 2: [], 3: []}
    for _ in range(4):
        ms = [r.randint(1, 100), r.randint(1, 100)]
        T[1].append(fmt(ms, rq(r, ms, 100, 10**5)))
    T[1].append(fmt([10, 12], rq(r, [10, 12], 100, 10**5)))
    def msprod(k, lim):
        ms = []; P = 1
        for _ in range(k):
            m = r.randint(1, max(1, min(10**6, lim // P)))
            ms.append(m); P *= m
        return ms
    for _ in range(3):
        ms = msprod(r.randint(1, 20), 10**18)
        T[2].append(fmt(ms, rq(r, ms, 10**5, 10**18)))
    T[2].append(fmt([999983, 999979, 999961], rq(r, [999983, 999979, 999961], 10**5, 10**18)))
    for _ in range(2):
        ms = [r.randint(1, 10**6) for _ in range(20)]
        T[3].append(fmt(ms, rq(r, ms, 10**5, 10**18)))
    ms = [r.choice([2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 36, 720720, 997, 999983]) for _ in range(20)]
    T[3].append(fmt(ms, rq(r, ms, 10**5, 10**18)))
    ms = [999983 - 2 * i for i in range(20)]
    T[3].append(fmt(ms, rq(r, ms, 10**5, 10**18)))
    T[3].append(fmt([1] * 20, rq(r, [1] * 20, 10**5, 10**18)))
    return T
def small(r):
    k = r.randint(1, 4); ms = [r.randint(1, 12) for _ in range(k)]
    return fmt(ms, rq(r, ms, 10, r.choice([200, 10**18])))
