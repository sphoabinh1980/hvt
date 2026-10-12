import random, math
def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%d %d %d %d\n' % x for x in qs)
def rq(r, A, Pm, Q, cop=False):
    out = []
    while len(out) < Q:
        p1, p2 = r.randint(1, Pm), r.randint(1, Pm)
        if r.random() < 0.4 and not cop:
            g = r.randint(1, 50); p1 = max(1, p1 // g * g); p2 = max(1, p2 // g * g)
        if cop and math.gcd(p1, p2) != 1: continue
        if cop: a1, a2 = r.randrange(p1), r.randrange(p2)
        else:
            a1, a2 = r.randint(0, A), r.randint(0, A)
            if r.random() < 0.5:
                g = math.gcd(p1, p2); a2 = a1 + g * r.randint(0, 10) if a1 + g * 10 <= A else a2
        out.append((a1, p1, a2, p2))
    return out
def samples():
    return [(fmt([(2, 3, 3, 5), (1, 4, 2, 6), (10, 4, 0, 6)]), '8\n-1\n18\n'),
            (fmt([(0, 10**9, 999999999, 999999999), (10**18, 2, 7, 1)]), '999999999000000000\n1000000000000000000\n')]
def tests():
    r = random.Random(122)
    return {1: [fmt(rq(r, 1000, 1000, 1000)), fmt([(1000, 1, 0, 1000), (999, 1000, 1000, 999), (10, 4, 0, 6), (0, 1, 0, 1), (500, 2, 1, 2)] * 20)],
            2: [fmt(rq(r, 0, 10**9, 10**5, True)), fmt([(0, 10**9, 999999998, 999999999)] * 10**5)],
            3: [fmt(rq(r, 10**18, 10**9, 10**5)), fmt([(10**18 - r.randint(0, 10**9), r.randint(1, 10**9), r.randint(0, 10**18), r.randint(1, 10**9)) for _ in range(10**5)]),
                fmt([(10**18, 2, 7, 1), (0, 10**9, 999999999, 999999999), (10**18, 10**9, 10**18, 10**9 - 1)] * 33333)]}
def small(r):
    return fmt(rq(r, 60, 12, 10))
