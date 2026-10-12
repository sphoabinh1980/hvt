import random
P = 10**9 + 7
def samples():
    return [('4 1\n', '8\n'), ('5 4\n', '0\n'), ('1000000000000000000 999999999999999990\n', '513687792\n')]
def T(n, k): return '%d %d\n' % (n, n - k)
def tests():
    r = random.Random(143)
    return {1: [T(n, r.randint(0, n)) for n in range(1, 9)] + [T(8, 8), T(8, 0), T(1, 1), T(7, 1)],
            2: [T(10**6, 10**6), T(10**6, 999999), T(999983, 500000), T(r.randint(1, 10**6), r.randint(0, 1000)), T(10**6, 0)],
            3: [T(10**18, 10**7), T(10**18 - 7, 9999999), T(P * 123456789 + 5, 1000), T(P * 999 + 10**7 - 1, 10**7),
                T(r.randint(10**17, 10**18), r.randint(10**6, 10**7)), T(10**18, 1), T(10**18, 0), T(P + 3, 2), T(10**10, 10**7)]}
def small(r):
    t = r.random()
    if t < 0.3: n = r.randint(1, 30); return T(n, r.randint(0, n))
    if t < 0.6: n = P * r.randint(1, 10**8) + r.randint(0, 40); return T(n, r.randint(0, min(n, 60)))
    n = r.randint(1, 10**18); return T(n, r.randint(0, 60))
