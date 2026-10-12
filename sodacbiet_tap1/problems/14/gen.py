import random
def samples():
    return [('1432219 3\n', '1219\n'), ('10200 1\n', '200\n'), ('2026 1\n', '26\n'), ('10 2\n', '0\n')]
def rnd(r, L, digs='0123456789'):
    return str(r.randint(1, 9)) + ''.join(r.choice(digs) for _ in range(L - 1))
def tests():
    r = random.Random(14)
    return {1: ['%s %d\n' % (rnd(r, 3000), r.randint(0, 3000)) for _ in range(3)],
            2: ['%s %d\n' % (rnd(r, 10**6), 5 * 10**5), '%s %d\n' % ('1' + '9' * (10**6 - 1), 10**6 - 1), '%s %d\n' % (''.join(str(i % 10) for i in range(1, 10**6 + 1)), 5 * 10**5),
                '%s %d\n' % ('9' * (10**6 // 2) + '1' * (10**6 // 2), 10**6 // 2), '%s %d\n' % (rnd(r, 10**6, '01'), 999), '%s %d\n' % ('1' + '0' * (10**6 - 1), 1)]}
def small(r):
    L = r.randint(1, 12); s = rnd(r, L, r.choice(['0123456789', '01', '019']))
    return '%s %d\n' % (s, r.randint(0, L))
