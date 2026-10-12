import random
def fmt(n, xs):
    return '%d %d\n%s\n' % (n, len(xs), ' '.join(map(str, xs)))
def divs(n):
    a, b = [], []
    d = 1
    while d * d <= n:
        if n % d == 0:
            a.append(d)
            if d * d != n: b.append(n // d)
        d += 1
    return a + b[::-1]
def qs(r, n, Q, near=False):
    out = []
    ds = divs(n) if n <= 10**12 else None
    for _ in range(Q):
        t = r.random()
        if t < 0.15: out.append(r.randint(1, 10**12))
        elif t < 0.3: out.append(n + r.randint(0, 5))
        elif near or t < 0.7: out.append(max(1, ds[-1 - r.randint(0, min(3, len(ds) - 1))] - r.randint(0, 1)))
        else: out.append(r.randint(1, n))
    return out
def samples():
    return [(fmt(36, [5, 10, 36, 40]), '9\n1 2 3 4 6 9 12 18 36\n6\n12\n36\n-1\n'),
            (fmt(999999999989, [2, 10**12]), '2\n1 999999999989\n999999999989\n-1\n'),
            (fmt(1, [1, 2]), '1\n1\n1\n-1\n')]
def tests():
    r = random.Random(22)
    T = {1: [], 2: [], 3: []}
    for n in [1, 720720, 999983, 10**6, 963761]:
        T[1].append(fmt(n, qs(r, n, 100)))
    for n in [963761198400, 10**12, 999999999989, 999966000289, 735134400000, r.randint(1, 10**12)]:
        T[2].append(fmt(n, qs(r, n, 100)))
    for n in [963761198400, 897612484786617600 // 10**6 if False else 963761198400, 748010118400, 10**12, 999999999989, 1]:
        T[3].append(fmt(n, qs(r, n, 10**5, near=True)))
    T[3].append(fmt(963761198400, [963761198400 - r.randint(0, 1) for _ in range(10**5)]))
    T[3].append(fmt(963761198400, [10**12] * 10**5))
    return T
def small(r):
    n = r.randint(1, 3000)
    return fmt(n, [r.randint(1, n + 3) for _ in range(r.randint(1, 30))])
