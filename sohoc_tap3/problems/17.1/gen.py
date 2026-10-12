import random, sys
sys.set_int_max_str_digits(0)
def num(r, L, neg=False):
    s = str(r.randint(1, 9)) + ''.join(r.choice('0123456789') for _ in range(L - 1))
    return ('-' if neg else '') + s
def P(a, b): return '%s\n%s\n' % (a, b)
def samples():
    return [(P(98765, 4789), '103554\n'), (P(10**20, -1), '99999999999999999999\n'), (P(-2026, 2026), '0\n')]
def tests():
    r = random.Random(171)
    L = 10**5
    big = num(r, L)
    return {1: [P(10**18, 10**18), P(-10**18, 10**18), P(-9, 10), P(r.randint(-10**18, 10**18), r.randint(-10**18, 10**18)), P(-10**18, -10**18), P(0, 0), P(123, -999999999999999999)],
            2: [P(num(r, L), num(r, L)), P('9' * L, '1'), P('0', num(r, L)), P(num(r, L), num(r, 5)), P('9' * L, '9' * L)],
            3: [P('-' + big, big), P('1' + '0' * (L - 1), '-1'), P('-' + '9' * (L - 1), '1' + '0' * (L - 1)), P(num(r, L, True), num(r, L)),
                P(num(r, L, True), num(r, L, True)), P('-' + big[:-1] + str((int(big[-1]) + 1) % 10), big), P('-9', '1' + '0' * (L - 1)), P('-' + '1' + '0' * (L - 1), '9' * (L - 1))]}
def small(r):
    def x():
        L = r.randint(1, 25); s = num(r, L) if r.random() < 0.9 else '0'
        return s if s == '0' or r.random() < 0.5 else '-' + s
    a = x()
    b = x() if r.random() < 0.8 else (a[1:] if a[0] == '-' else ('-' + a if a != '0' else '0'))
    return P(a, b)
