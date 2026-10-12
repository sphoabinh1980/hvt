import random
def samples():
    return [('300 0\n', '1\n220 284\n'), ('200 1\n', '2\n48 75\n140 195\n'), ('283 0\n', '0\n')]
def tests():
    r = random.Random(23)
    T = {1: ['2000 0\n', '2000 1\n', '2000 2\n', '1 0\n', '%d %d\n' % (r.randint(1, 2000), r.randint(0, 50)), '2000 10000000\n'],
         2: ['200000 0\n', '200000 1\n', '200000 3\n', '199999 7\n', '200000 10000000\n', '%d %d\n' % (r.randint(1, 200000), r.randint(0, 20))],
         3: ['10000000 0\n', '10000000 1\n', '10000000 2\n', '9999999 5\n', '10000000 10000000\n', '%d %d\n' % (r.randint(5000000, 10000000), r.randint(0, 12))]}
    return T
def small(r):
    return '%d %d\n' % (r.randint(1, 1500), r.choice([0, 1, 2, 3, r.randint(0, 100)]))
