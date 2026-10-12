import random
from sympy import prevprime, nextprime
def fmt(xs):
    return '%d\n' % len(xs) + ''.join('%d\n' % x for x in xs)
def big(r, lim):
    t = r.random()
    if t < 0.2:
        p = prevprime(r.randint(10**4 + 2, int(lim ** 0.5)))
        return p * p * r.randint(1, max(1, lim // (p * p)))
    if t < 0.4:
        p = prevprime(r.randint(10**4 + 2, 10**6)); q = prevprime(r.randint(10**4 + 2, lim // p))
        return p * q
    if t < 0.55:
        return prevprime(r.randint(3, lim))
    if t < 0.7:
        p = prevprime(r.randint(10**4 + 2, int(lim ** (1 / 3)) * 3 if lim > 10**9 else 10**4 + 50))
        return min(lim, p * p) if r.random() < 0.5 else p
    return r.randint(1, lim)
def samples():
    return [(fmt([4, 36, 360, 30, 1, 3600]), '1\n2\n2\n0\n0\n3\n'),
            (fmt([999966000289, 10**12, 995303515103, 998696708677, 100160063]), '1\n2\n1\n1\n0\n')]
def tests():
    r = random.Random(63)
    T = {1: [fmt([r.randint(1, 10**6) for _ in range(10**5)]), fmt([997 * 997, 999983, 10**6, 720720, 1, 4, 9, 25 * 49, 991 * 991, 1009 * 991] * 10**4)],
         2: [fmt([big(r, 10**12) for _ in range(100)]), fmt([999966000289, 999999999989, 999962000357, 10**12, 963761198400] * 20)],
         3: [fmt([big(r, 10**12) for _ in range(10**5)]), fmt([999999999989] * 50000 + [999966000289] * 50000), fmt([r.randint(1, 10**12) for _ in range(10**5)])]}
    return T
def small(r):
    return fmt([big(r, 10**12) if r.random() < 0.7 else r.randint(1, 10**6) for _ in range(30)])
