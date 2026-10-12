import random
def samples():
    return [('1 100\n', '5\n'), ('100 1000\n', '15\n'), ('1 1000000000000\n', '47995\n')]
def tests():
    r = random.Random(17)
    s1 = ['1 10000000\n', '1 1\n', '10 12\n', '%d %d\n' % (r.randint(1, 10**6), 10**7), '9000000 10000000\n', '%d %d\n' % (r.randint(1, 10**5), r.randint(10**6, 10**7))]
    s2 = ['1 1000000000000\n', '100000000000 1000000000000\n', '%d %d\n' % (r.randint(1, 10**11), 10**12), '%d %d\n' % (r.randint(10**8, 10**9), r.randint(10**10, 10**11)),
          '10000000000 99999999999\n', '1 999999999999\n']
    return {1: s1, 2: s2}
def small(r):
    a = r.randint(1, 200000); return '%d %d\n' % (a, a + r.randint(0, r.choice([100, 20000, 300000])))
