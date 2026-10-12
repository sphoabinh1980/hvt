import random
def fmt(a):
    return '%d\n%s\n' % (len(a), ' '.join(map(str, a)))
def mk(r, n, g, bad, lim=10**18):
    a = [g * r.randint(1, lim // g) for _ in range(n)]
    for _ in range(bad):
        a[r.randrange(n)] = r.randint(1, lim)
    return a
def samples():
    return [(fmt([12, 18, 7, 24, 30]), '6 3\n'), (fmt([4, 6]), '6 1\n'), (fmt([5, 5, 5]), '5 1\n')]
def tests():
    r = random.Random(32)
    T = {1: [fmt(mk(r, 3000, 6, 1)), fmt(mk(r, 3000, 10**9, 1)), fmt(mk(r, 3000, 2**40, 0)), fmt(mk(r, 3000, 1, 0)),
             fmt([10**18] * 3000), fmt(mk(r, 2, 1, 0)), fmt(mk(r, 3000, 999999937, 2))],
         2: [fmt(mk(r, 500000, 6, 1)), fmt(mk(r, 500000, 10**9 + 7, 1)), fmt(mk(r, 500000, 1, 0)), fmt([10**18] * 500000),
             fmt(mk(r, 500000, 2**50, 1)), fmt([2 * 3 * 5 * 7 * 11 * 13 * r.randint(1, 10**13) for _ in range(499999)] + [997])]}
    return T
def small(r):
    n = r.randint(2, 12)
    g = r.randint(1, 30)
    return fmt(mk(r, n, g, r.randint(0, 2), 600))
