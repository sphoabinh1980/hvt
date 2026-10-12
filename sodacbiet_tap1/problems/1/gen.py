import random
def samples():
    return [('12\n', '51\n'), ('100\n', '901\n'), ('2026\n', '28189\n')]
def tests():
    r = random.Random(1)
    return {1: ['%d\n' % r.randint(1, 10**7), '10000000\n', '1\n'], 2: ['1000000000000000\n', '%d\n' % r.randint(10**14, 10**15), '999999999999999\n']}
def small(r):
    return '%d\n' % r.randint(1, 5000)
