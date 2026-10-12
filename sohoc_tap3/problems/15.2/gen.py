import random
def T(n, bs):
    bs = list(bs); random.Random(len(bs) + n % 997).shuffle(bs)
    return '%d %d\n' % (n, len(bs)) + (' '.join(map(str, bs)) + '\n' if bs else '')
def samples():
    return [('5 0\n', '13\n'), ('6 2\n4 2\n', '4\n'), ('1000000000000000000 3\n7 5 6\n', '0\n')]
def tests():
    r = random.Random(152)
    return {1: [T(10**6, r.sample(range(1, 10**6), 10**4)), T(10**6, []), T(999999, r.sample(range(1, 999999, 2), 5000)), T(1, [1]), T(3, [1, 2]),
                T(10**6, [10**6 - 1, 10**6 - 2])],
            2: [T(10**18, []), T(r.randint(1, 10**18), []), T(1, []), T(2, []), T(3, []), T(10**18 - 1, [])],
            3: [T(10**18, r.sample(range(1, 10**18), 10**4)), T(10**18, sorted(r.sample(range(1, 10**18), 9999)) + [10**18]),
                T(r.randint(10**17, 10**18), [x for x in range(1, 20001, 2)]), T(10**18, [5 * 10**17, 5 * 10**17 + 1]),
                T(10**18, [10**18 - 2, 10**18 - 1]), T(10**18, [3 * 10**17, 3 * 10**17 + 1, 3 * 10**17 + 2])]}
def small(r):
    n = r.randint(1, 60)
    return T(n, r.sample(range(1, n + 1), r.randint(0, min(n, 6))))
