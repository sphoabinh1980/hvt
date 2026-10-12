import random
from sympy import prevprime
def fmt(cases):
    return '%d\n' % len(cases) + ''.join('%d %d\n%s\n' % (len(a), m, ' '.join(map(str, a))) for m, a in cases)
def samples():
    return [(fmt([(1000, [2, 3, 2]), (12, [2, 10, 18]), (7, [2, 0, 0, 5])]), '512\n4\n2\n'),
            (fmt([(1000, [3, 3, 3, 3]), (1000000007, [2, 2, 2, 2, 2]), (1, [5])]), '387\n973586826\n0\n')]
def tower_ok(a, lim=10**18):
    E = a[-1]
    for x in reversed(a[:-1]):
        if x <= 1: E = 1 if (x == 1 or E == 0) else 0; continue
        if E > 64: return False
        E = x ** E
        if E > lim: return False
    return True
def tests():
    r = random.Random(113)
    T = {1: [], 2: [], 3: [], 4: []}
    c1 = []
    while len(c1) < 10:
        k = r.randint(1, 3); a = [r.choice([0, 1, 2, 3, 10, r.randint(0, 10**9)]) for _ in range(k)]
        if tower_ok(a): c1.append((r.randint(1, 10**9), a))
    T[1].append(fmt(c1))
    man = [(12, [2, 3, 3]), (10**9, [10**9, 2]), (10**9, [10**9]), (36, [6, 2, 4]), (1, [3, 3]), (7, [0, 0]), (8, [2, 3, 2]), (10**9, [0, 5, 0]), (1000, [999999999, 1, 10**9]), (64, [2, 2, 5]), (999999937, [3, 3, 3])]
    T[1].append(fmt([c for c in man if tower_ok(c[1])]))
    c2 = []
    while len(c2) < 10:
        m = prevprime(r.randint(3, 10**9)); a1 = r.randint(1, 10**9)
        if a1 % m: c2.append((m, [a1, r.randint(1, 10**9), r.randint(0, 10**9)]))
    T[2].append(fmt(c2))
    T[3].append(fmt([(r.randint(1, 10**9), [r.randint(0, 10**9), r.randint(1, 10**9), r.randint(0, 10**9)]) for _ in range(10)]))
    T[3].append(fmt([(m, [a, r.randint(1, 10**9), r.randint(0, 10**9)]) for m, a in [(12, 2), (2**29, 6), (10**9, 10), (3 ** 18, 3), (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23, 30), (999999937 * 1, 999999937), (1000, 2), (10**9, 2), (36, 6), (64, 2)]]))
    T[4].append(fmt([(r.randint(1, 10**9), [r.randint(0, 10**9) for _ in range(10**5)]) for _ in range(10)]))
    T[4].append(fmt([(r.randint(1, 10**9), [r.choice([0, 1, 2, 2, 3, r.randint(0, 10**9)]) for _ in range(r.randint(1, 10**5))]) for _ in range(10)]))
    T[4].append(fmt([(10**9, [2] * 10**5), (999999937, [3] * 10**5), (2**29, [2, 0, 0] * 33333), (1000, [10, 1, 0, 5]), (10**9, [0] * 10**5), (10**9, [1] * 10**5), (12, [2, 3, 0, 0]), (10**9, [2, 2, 2, 2, 2]), (7 * 2**26, [14] * 10**5), (1, [5] * 10)]))
    return T
def small(r):
    cases = []
    for _ in range(10):
        if r.random() < 0.5:
            k = r.randint(1, 4); a = [r.randint(0, 3) for _ in range(k)]
        else:
            k = r.randint(1, 3); a = [r.randint(0, 12) for _ in range(k)]
            if k == 3 and a[1] ** a[2] > 10**9: a[2] = r.randint(0, 3)
        cases.append((r.randint(1, 300), a))
    return fmt(cases)
