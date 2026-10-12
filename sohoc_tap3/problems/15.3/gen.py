import random
def G(n, E, Q):
    return '%d %d %d\n' % (n, len(E), len(Q)) + ''.join('%d %d\n' % e for e in E) + ''.join('%d %d %d\n' % x for x in Q)
def rgraph(r, n, p):
    return [(u, v) for u in range(1, n + 1) for v in range(1, n + 1) if r.random() < p]
def samples():
    E = [(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), (3, 4), (4, 3)]
    return [(G(4, E, [(1, 3, 3), (1, 1, 2), (4, 4, 0)]), '4\n2\n1\n'), (G(2, [(1, 1), (1, 2), (2, 1)], [(1, 1, 10), (1, 2, 10**18)]), '89\n209783453\n')]
def tests():
    r = random.Random(153)
    full = [(u, v) for u in range(1, 51) for v in range(1, 51)]
    def qs(cnt, kmax): return [(r.randint(1, 50), r.randint(1, 50), r.choice([0, 1, r.randint(0, kmax)])) for _ in range(cnt)]
    return {1: [G(50, full, qs(10, 1000)), G(50, rgraph(r, 50, 0.3), qs(10, 1000))],
            2: [G(50, full, qs(10, 10**18)), G(50, rgraph(r, 50, 0.5), [(1, 2, 10**18 - i) for i in range(10)])],
            3: [G(50, full, qs(1000, 10**18)), G(50, rgraph(r, 50, 0.2), qs(1000, 10**18)), G(50, rgraph(r, 50, 0.05), [(r.randint(1, 50), r.randint(1, 50), 2**60 - 1 - r.randint(0, 10**6)) for _ in range(1000)]),
                G(1, [(1, 1)], [(1, 1, 10**18)] * 1000)]}
def small(r):
    n = r.randint(1, 5)
    E = rgraph(r, n, r.random())
    return G(n, E, [(r.randint(1, n), r.randint(1, n), r.randint(0, 25)) for _ in range(10)])
