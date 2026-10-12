import random
def fmt(m, n, cells):
    return '%d %d %d\n' % (m, n, len(cells)) + ''.join('%d %d\n' % c for c in cells)
def cells(r, m, n, K, mode=None):
    out = []
    while len(out) < K:
        if mode == 'chain' and out:
            x0, y0 = out[0]
            c = (r.randint(0, x0), r.randint(0, y0)) if r.random() < 0.5 else (r.randint(x0, m), r.randint(y0, n))
        else:
            c = (r.randint(0, m), r.randint(0, n))
        if c not in out: out.append(c)
    return out
def samples():
    return [(fmt(3, 2, [(1, 1)]), '4\n'), (fmt(4, 3, [(3, 2), (1, 1)]), '7\n'), (fmt(2, 2, [(1, 0), (0, 1)]), '0\n')]
def tests():
    r = random.Random(132)
    T = {1: [fmt(1000, 1000, cells(r, 1000, 1000, 2, 'chain')), fmt(1000, 999, cells(r, 1000, 999, 1)), fmt(1000, 1000, []), fmt(r.randint(0, 1000), r.randint(0, 1000), cells(r, 0, 0, 0)),
             fmt(1000, 1000, [(0, 0)]), fmt(1000, 1000, [(1000, 1000), (3, 4)]), fmt(0, 0, [])],
         2: [fmt(10**6, 10**6, []), fmt(10**6, 10**6, cells(r, 10**6, 10**6, 1)), fmt(r.randint(0, 10**6), r.randint(0, 10**6), []), fmt(10**6, 10**6, [(500000, 500000)]), fmt(10**6, 0, [(5, 0)])],
         3: [fmt(10**6, 10**6, cells(r, 10**6, 10**6, 2, 'chain')) for _ in range(3)] + [fmt(10**6, 10**6, cells(r, 10**6, 10**6, 2)) for _ in range(2)] +
            [fmt(10**6, 10**6, [(700000, 800000), (100000, 200000)]), fmt(10**6, 10**6, [(10**6, 10**6), (0, 0)]), fmt(10**6, 10**6, [(999999, 3), (2, 999998)])]}
    return T
def small(r):
    m, n = r.randint(0, 8), r.randint(0, 8)
    K = r.randint(0, min(2, (m + 1) * (n + 1)))
    return fmt(m, n, cells(r, m, n, K, r.choice([None, 'chain'])))
