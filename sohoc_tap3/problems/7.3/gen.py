import random
from sympy import prevprime
def fmt(a):
    return '%d\n%s\n' % (len(a), ' '.join(map(str, a)))
def samples():
    return [(fmt([4, 6, 9, 10, 4]), '180\n2\n'), (fmt(list(range(1, 21))), '232792560\n5\n'), (fmt([9999991, 9999973, 9999991, 1]), '639300250\n1\n')]
def tests():
    r = random.Random(73)
    T = {1: [fmt([r.randint(1, 50) for _ in range(20)]) for _ in range(3)] + [fmt([1]), fmt([50]), fmt(list(range(31, 51))), fmt([r.choice([16, 27, 25, 49, 32, 1, 2, 3]) for _ in range(20)])],
         2: [fmt([r.randint(1, 10**7) for _ in range(2000)]), fmt([r.randint(1, 1000) for _ in range(2000)]), fmt([2 ** r.randint(0, 20) * 3 ** r.randint(0, 2) for _ in range(2000)]),
             fmt([prevprime(r.randint(3, 10**7)) for _ in range(2000)])],
         3: [fmt([r.randint(1, 10**7) for _ in range(10**5)]), fmt([r.randint(1, 1000) for _ in range(10**5)]), fmt([prevprime(r.randint(10**6, 10**7)) for _ in range(10**5)]),
             fmt([2 ** r.randint(0, 23) for _ in range(10**5)]), fmt([9699690] * 99999 + [8388608]), fmt([1] * 10**5)]}
    return T
def small(r):
    n = r.randint(1, 10)
    return fmt([r.choice([r.randint(1, 60), 2 ** r.randint(0, 6), 3 ** r.randint(0, 4)]) for _ in range(n)])
