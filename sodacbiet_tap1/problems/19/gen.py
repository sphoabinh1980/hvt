import random
def samples():
    return [('5\n25\n2026\n3\n50\n325\n', '2\n1\n0\n2\n3\n')]
def tests():
    r = random.Random(19)
    def mk(q, hi, special=()):
        xs = list(special) + [r.randint(1, hi) for _ in range(q - len(special))]
        return '%d\n' % q + '\n'.join(map(str, xs)) + '\n'
    sp = [1, 2, 4, 5, 25, 50, 65, 325, 1105, 9999991, 10**7, 5**10, 2 * 5**9, 9765625 , 4 * 1999999]
    return {1: [mk(1000, 10**7, sp), mk(1000, 10**7), mk(1000, 1000), mk(1, 1)],
            2: [mk(10**6, 10**7, sp), mk(10**6, 10**7), mk(10**6, 10**7, [10**7] * 1000), mk(500000, 10**6)]}
def small(r):
    q = r.randint(1, 50)
    return '%d\n' % q + '\n'.join(str(r.randint(1, r.choice([100, 10**4, 10**7]))) for _ in range(q)) + '\n'
