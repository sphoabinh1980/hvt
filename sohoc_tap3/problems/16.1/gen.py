import random
def samples():
    return [('20\n', '339\n'), ('1000000000000\n', '146462362\n')]
def tests():
    r = random.Random(161)
    return {1: ['1\n', '10000\n', '%d\n' % r.randint(1, 10**4), '9973\n'],
            2: ['10000000\n', '%d\n' % r.randint(10**6, 10**7), '9999991\n'],
            3: ['1000000000000\n', '%d\n' % r.randint(10**11, 10**12), '999999999999\n', '%d\n' % r.randint(10**9, 10**10), '2000000014\n', '1000000006\n']}
def small(r):
    return '%d\n' % r.randint(1, 1500)
