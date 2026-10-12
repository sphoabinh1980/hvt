import random
def samples():
    return [('12 1000\n', '112\n'), ('15 7\n', '2\n')]
def tests():
    r = random.Random(13)
    T = {1: ['%d %d\n' % (n, m) for n, m in [(1, 1), (9, 1000000000), (9, 7), (5, 2), (r.randint(1, 9), r.randint(1, 10**9)), (8, 999999937)]],
         2: ['%d %d\n' % (n, m) for n, m in [(1000, 10**9), (1000, 999999937), (999, 1), (r.randint(10, 1000), r.randint(1, 10**9)), (100, 3), (1000, 2**29)]],
         3: ['%d %d\n' % (n, m) for n, m in [(10**7, 10**9), (10**7, 999999937), (9999999, 1000000007 - 8), (10**7, 1), (r.randint(10**6, 10**7), r.randint(1, 10**9)), (123456, 99991), (10**7, 3)]]}
    return T
def small(r):
    return '%d %d\n' % (r.randint(1, 300), r.randint(1, 10**9))
