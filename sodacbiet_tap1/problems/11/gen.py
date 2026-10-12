import random
def F(q): return '%d\n' % len(q) + ''.join('%d %d\n' % x for x in q)
def samples():
    return [(F([(7, 5), (4, 3), (2025, 10**18)]), '1\n58\n145\n')]
def tests():
    r = random.Random(11)
    return {1: [F([(r.randint(1, 10**18), r.randint(0, 10**6)) for _ in range(10)])],
            2: [F([(r.randint(1, 10**18), r.randint(0, 10**18)) for _ in range(10**5)]), F([(10**18, 10**18), (1, 10**18), (4, 10**18 - 1), (999999999999999999, 0)] * 10)]}
def small(r):
    return F([(r.randint(1, 10**18) if r.random() < 0.5 else r.randint(1, 200), r.randint(0, 60)) for _ in range(20)])
