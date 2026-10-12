import random
def F(q): return '%d\n' % len(q) + ''.join('%d %d %d\n' % x for x in q)
def samples():
    return [(F([(1, 100, 1), (2026, 2026, 1), (1, 10**18, 9)]), '12\n1\n111111111111111111\n')]
def rq(r, M):
    a, b = r.randint(1, M), r.randint(1, M); return (min(a, b), max(a, b), r.randint(1, 9))
def tests():
    r = random.Random(6)
    return {1: [F([rq(r, 10**5) for _ in range(10)])], 2: [F([rq(r, 10**18) for _ in range(10**5)]), F([(1, 10**18, k) for k in range(1, 10)] + [(10**18, 10**18, 1)])]}
def small(r):
    return F([rq(r, 2000) for _ in range(20)])
