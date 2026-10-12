import random
def samples():
    return [('100\n', '33\n'), ('2026\n', '410\n'), ('1000000\n', '95428\n')]
def tests():
    r = random.Random(16)
    return {1: ['%d\n' % x for x in [10**6, 999999, r.randint(1, 10**6), r.randint(1, 10**5), 1, 12]],
            2: ['%d\n' % x for x in [10**18, 10**18 - 1, r.randint(1, 10**18), r.randint(10**17, 10**18), r.randint(1, 10**12), 2026 * 10**14, 999999999999999998]]}
def small(r):
    return '%d\n' % r.randint(1, r.choice([100, 5000, 200000]))
