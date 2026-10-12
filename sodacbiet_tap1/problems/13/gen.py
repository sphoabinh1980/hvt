import random
def samples():
    return [('2026\n', '2062\n'), ('4321\n', '-1\n'), ('1987654320\n', '2013456789\n')]
def rnd(r, L, digs='0123456789'):
    return str(r.randint(1, 9)) + ''.join(r.choice(digs) for _ in range(L - 1))
def tests():
    r = random.Random(13)
    return {1: ['%d\n' % x for x in [r.randint(1, 10**6), 999999, 100000, 987654, 102, 7]],
            2: [rnd(r, 10**6) + '\n', '9' * 10**6 + '\n', '1' + '9' * (10**6 - 1) + '\n', ''.join(sorted(rnd(r, 10**6), reverse=True)) + '\n',
                rnd(r, 10**6, '01') + '\n', '1' + '0' * (10**6 - 1) + '\n']}
def small(r):
    return rnd(r, r.randint(1, 7), r.choice(['0123456789', '012', '19'])) + '\n'
