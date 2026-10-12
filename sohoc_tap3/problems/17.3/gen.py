import random
def num(r, L, neg=False):
    s = str(r.randint(1, 9)) + ''.join(r.choice('0123456789') for _ in range(L - 1))
    return ('-' if neg else '') + s
def P(a, b): return '%s\n%s\n' % (a, b)
def samples():
    return [(P(123, 45), '5535\n'), (P(-99999999, 99999999), '-9999999800000001\n'), (P(0, -12345), '0\n')]
def tests():
    r = random.Random(173)
    return {1: [P(10**18, 10**18), P(-10**18, 999999999999999999), P(0, -10**18), P(-1, -1), P(r.randint(-10**18, 10**18), r.randint(-10**18, 10**18))],
            2: [P('9' * 5000, '9' * 5000), P(num(r, 5000, True), num(r, 5000)), P(num(r, 4999), num(r, 3)), P('-' + '1' + '0' * 4999, '-' + '9' * 5000)],
            3: [P('9' * 50000, '9' * 50000), P(num(r, 50000, True), num(r, 50000, True)), P(num(r, 50000), num(r, 1)), P('-' + num(r, 50000), '0'),
                P('1' + '0' * 49999, '-' + num(r, 49998))]}
def small(r):
    def x():
        if r.random() < 0.1: return '0'
        s = num(r, r.randint(1, 40)); return s if r.random() < 0.5 else '-' + s
    return P(x(), x())
