import random

def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%s %s\n' % x for x in qs)

def big(r, L, mult4=None):
    s = str(r.randint(1, 9)) + ''.join(r.choice('0123456789') for _ in range(L - 1))
    if mult4 is not None:
        x = int(s[-2:])
        x = x - x % 4 + mult4
        if x >= 100: x -= 4
        s = s[:-2] + '%02d' % x if L >= 2 else s
    return s

def samples():
    return [(fmt([(2, 2026), (7, 3), (0, 0)]), '4\n3\n1\n'),
            (fmt([('123456789123456789123456789', '98765432109876543210')]), '1\n')]

def tests():
    r = random.Random(12)
    T = {1: [], 2: [], 3: []}
    T[1].append(fmt([(r.randint(0, 20), r.randint(0, 20)) for _ in range(10)]))
    T[1].append(fmt([(r.randint(0, 10**6), r.randint(0, 10**6)) for _ in range(10)]))
    T[1].append(fmt([(r.randint(0, 10**6), 4 * r.randint(1, 250000)) for _ in range(10)]))
    T[1].append(fmt([(0, 0), (0, 5), (10**6, 10**6), (999999, 1000000), (2, 4), (3, 8), (7, 12), (8, 1000000), (9, 0), (1, 999999)]))
    T[2].append(fmt([(r.randint(0, 10**18), r.randint(0, 10**18)) for _ in range(10)]))
    T[2].append(fmt([(r.randint(0, 10**18), 4 * r.randint(1, 10**17)) for _ in range(10)]))
    T[2].append(fmt([(10**18, 10**18), (2, 10**18), (3, 10**18 - 1), (7, 10**18 - 2), (0, 0), (12, 999999999999999996), (999999999999999999, 2), (5, 10**18), (6, 1), (4, 10**18)]))
    for k in range(4):
        T[3].append(fmt([(big(r, 10**5), big(r, 10**5, mult4=r.choice([None, 0]))) for _ in range(10)]))
    T[3].append(fmt([(big(r, 10**5), '0'), ('0', big(r, 10**5)), ('0', '0'), (big(r, 1000), big(r, 10**5, mult4=0)), ('2', big(r, 10**5, mult4=0)), ('3', big(r, 10**5, mult4=0)), ('7', big(r, 10**5, mult4=0)), ('8', big(r, 10**5, mult4=0)), ('9', big(r, 10**5, mult4=1)), ('4', big(r, 10**5, mult4=2))]))
    return T

def small(r):
    return fmt([(r.randint(0, 30), r.randint(0, 30)) for _ in range(10)])
