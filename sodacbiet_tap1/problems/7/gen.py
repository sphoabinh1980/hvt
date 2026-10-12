import random
def samples():
    return [('3\n', '111\n'), ('12\n', '11100\n'), ('2026\n', '100001101010\n')]
def tests():
    r = random.Random(7)
    return {1: ['%d\n' % x for x in [1, 2, 7, 9, 11, 81, 99, r.randint(1, 100)]],
            2: ['%d\n' % x for x in [999999, 999998, 1000000, 999993, 98767, r.randint(10**5, 10**6), 99999]]}
def small(r):
    return '%d\n' % r.randint(1, 150)
