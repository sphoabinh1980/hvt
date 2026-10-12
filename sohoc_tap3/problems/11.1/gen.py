import random
from sympy import prevprime
def fmt(xs):
    return '%d\n' % len(xs) + ''.join('%d\n' % x for x in xs)
def samples():
    return [(fmt([12, 7, 1]), '4\n6\n1\n'), (fmt([10**12, 999999999989]), '400000000000\n999999999988\n')]
def tests():
    r = random.Random(111)
    T = {1: [fmt([r.randint(1, 10**4) for _ in range(100)]), fmt(list(range(1, 101))), fmt([9973, 10**4, 9999, 4096, 6561, 9991, 2, 1, 30, 9240] * 10)],
         2: [fmt([x]) for x in [999999999989, 10**12, 999966000289, 963761198400, 999999999999, 2 * 499999999979, 1, r.randint(1, 10**12)]],
         3: [fmt([prevprime(r.randint(10**11, 10**12)) for _ in range(100)]), fmt([r.randint(1, 10**12) for _ in range(100)]),
             fmt([2 * prevprime(r.randint(10**10, 5 * 10**11)) for _ in range(100)])]}
    return T
def small(r):
    return fmt([r.randint(1, 5000) for _ in range(20)])
