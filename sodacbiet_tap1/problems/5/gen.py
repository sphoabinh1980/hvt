import random
def F(S, m, qs): return '%s\n%d %d\n' % (S, m, len(qs)) + ''.join('%d %d\n' % x for x in qs)
def samples():
    return [(F('2026202620', 7, [(1, 4), (2, 5), (1, 10), (5, 5)]), '3\n3\n1\n2\n')]
def rnd(r, n): return ''.join(r.choice('0123456789') for _ in range(n))
def rq(r, n, k): 
    out = []
    for _ in range(k):
        a, b = r.randint(1, n), r.randint(1, n); out.append((min(a, b), max(a, b)))
    return out
def tests():
    r = random.Random(5)
    n1 = 3000; n2 = 10**6
    S1 = rnd(r, n1); S2 = rnd(r, n2); S3 = '9' * n2
    return {1: [F(S1, r.randint(1, 10**9), rq(r, n1, 3000)), F(S1, 7, rq(r, n1, 3000))],
            2: [F(S2, r.randint(1, 10**9), rq(r, n2, 10**6)), F(S3, 999999937, [(1, n2)] * 10**5 + rq(r, n2, 10**5)), F(S2, 1, rq(r, n2, 1000))]}
def small(r):
    n = r.randint(1, 40); S = rnd(r, n)
    return F(S, r.randint(1, 10**9) if r.random() < 0.5 else r.randint(1, 30), rq(r, n, 30))
