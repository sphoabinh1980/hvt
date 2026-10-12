import random
def F(q): return '%d\n' % len(q) + ''.join('%d %d\n' % x for x in q)
def samples():
    return [(F([(1, 100), (100, 2026), (1, 10**18)]), '18\n101\n1999999998\n')]
def rq(r, M):
    a, b = r.randint(1, M), r.randint(1, M); return (min(a, b), max(a, b))
def tests():
    r = random.Random(9)
    pals = [int(str(x) + str(x)[::-1]) for x in range(1, 50)]
    return {1: [F([rq(r, 10**6) for _ in range(10)])],
            2: [F([rq(r, 10**18) for _ in range(10**5)]), F([(1, 10**18), (10**18, 10**18), (999999999999999999, 10**18), (1, 9), (11, 11), (10, 10)] * 100),
                F([(p, p) for p in pals] + [(p + 1, p + 1) for p in pals] + [(r.randint(1, 10**k), 10**k) for k in range(1, 19)])]}
def small(r):
    return F([rq(r, 3000) for _ in range(20)] + [(10**k - 1, 10**k + 1) for k in range(1, 4)])
