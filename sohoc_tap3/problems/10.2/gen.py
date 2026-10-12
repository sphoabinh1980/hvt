import random
from sympy import prevprime, nextprime
def samples():
    return [('10 11\n', '0\n11\n'), ('6 1000000007\n', '650000007\n516764016\n'), ('1 2\n', '1\n1\n')]
def tests():
    r = random.Random(102)
    return {1: ['1000 %d\n' % prevprime(10**6), '%d %d\n' % (r.randint(1, 1000), prevprime(r.randint(1002, 10**6))), '1000 1009\n', '10 11\n', '1 2\n'],
            2: ['1000000 %d\n' % prevprime(2 * 10**9), '1000000 1000003\n', '%d %d\n' % (r.randint(1, 10**6), prevprime(r.randint(10**6 + 2, 2 * 10**9))), '999999 1000000007\n'],
            3: ['10000000 %d\n' % prevprime(2 * 10**9), '10000000 10000019\n', '10000000 1000000007\n', '%d %d\n' % (r.randint(10**6, 10**7), prevprime(r.randint(10**7 + 2, 2 * 10**9)))]}
def small(r):
    p = prevprime(r.randint(3, r.choice([1000, 2 * 10**9])))
    return '%d %d\n' % (r.randint(1, min(p - 1, 2000)), p)
