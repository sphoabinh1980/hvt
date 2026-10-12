import random
D = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def tob(v, a):
    r = ''
    while True:
        r = D[v % a] + r; v //= a
        if v == 0: return r
def q(r, a, b, lead=None, vmax=10**18):
    v = r.choice([0, 1, vmax, r.randint(0, vmax), r.randint(0, 1000)])
    s = tob(v, a)
    if lead is None: lead = r.random() < 0.5
    if lead: s = '0' * r.randint(1, 100 - len(s)) + s
    return (a, b, s)
def fmt(qs): return '%d\n' % len(qs) + ''.join('%d %d %s\n' % x for x in qs)
def samples():
    return [(fmt([(16, 8, '7EA'), (10, 2, '2026'), (36, 10, 'ZZ')]), '3752\n11111101010\n1295\n'),
            (fmt([(2, 16, '0000'), (7, 7, '00123'), (10, 36, '1000000000000000000')]), '0\n123\n7LIEEXZX4KXS\n')]
def tests():
    r = random.Random(181)
    return {1: [fmt([q(r, r.randint(2, 36), 10) for _ in range(10**5)]), fmt([(36, 10, '0' * 88 + 'ZZZZZZZZZZZZ'[:11] + '0'), (2, 10, '0' * 100)])],
            2: [fmt([q(r, 10, r.randint(2, 36), lead=False) for _ in range(10**5)]), fmt([(10, b, '0') for b in range(2, 37)])],
            3: [fmt([q(r, r.randint(2, 36), r.randint(2, 36)) for _ in range(10**5)]), fmt([(36, 2, '0' * 90 + tob(10**18, 36)), (2, 36, '0' * 40 + tob(10**18, 2))])]}
def small(r):
    return fmt([q(r, r.randint(2, 36), r.randint(2, 36)) for _ in range(30)])
