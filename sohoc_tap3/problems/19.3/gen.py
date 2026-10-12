import random
def G(k, a): return '%d %d %d\n' % (len(a), len(a[0]), k) + ''.join(' '.join(map(str, row)) + '\n' for row in a)
def R(r, m, n, M): return [[r.randint(-M, M) for _ in range(n)] for _ in range(m)]
def samples():
    return [(G(3, [[1, 2, 3], [4, 5, 6]]), '9\n'), (G(4, [[-1, 2, -3], [4, -5, 6], [-7, 8, -9]]), '8\n')]
def tests():
    r = random.Random(193)
    B = 10**9
    return {1: [G(r.randint(1, 10**6), R(r, 30, 30, B)), G(7, R(r, 30, 30, B)), G(1, R(r, 30, 30, 5)), G(10**6, [[0] * 30 for _ in range(30)])],
            2: [G(100, R(r, 400, 400, B)), G(97, R(r, 400, 400, B)), G(1, R(r, 400, 400, B)), G(2, R(r, 400, 400, 1))],
            3: [G(10**6, R(r, 400, 400, B)), G(999983, R(r, 400, 400, B)), G(10**6, [[0] * 400 for _ in range(400)]), G(1000, R(r, 400, 400, B)), G(500000, R(r, 400, 1, B))]}
def small(r):
    m, n = r.randint(1, 6), r.randint(1, 6)
    return G(r.randint(1, 10), R(r, m, n, 20))
