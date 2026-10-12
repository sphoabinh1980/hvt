import random
def samples():
    return [('300\n', '1\n220 284\n'), ('2000\n', '2\n220 284\n1184 1210\n'), ('100\n', '0\n')]
def tests():
    r = random.Random(18)
    return {1: ['%d\n' % x for x in [100000, 99999, 10, 1, r.randint(1, 10**5), 5564]],
            2: ['%d\n' % x for x in [10**7, 9999999, r.randint(10**6, 10**7), 5000000, 2 * 10**6]]}
def small(r):
    return '%d\n' % r.randint(1, r.choice([300, 20000, 100000]))
