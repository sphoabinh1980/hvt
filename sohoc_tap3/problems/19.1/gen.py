import random
def A(a): return '%d\n%s\n' % (len(a), ' '.join(map(str, a)))
def samples():
    return [(A([2, -7, 5, 4, -3, 1]), '2\n'), (A([0, 0, 0, 0]), '10\n'), (A([1, -1, 1, -1, 1]), '6\n')]
def tests():
    r = random.Random(191)
    B = 10**9
    return {1: [A([r.randint(-B, B) for _ in range(3000)]), A([r.choice([B, -B]) for _ in range(3000)]), A([r.randint(-3, 3) * B for _ in range(3000)])],
            2: [A([0] * 10**6), A([r.randint(-10, 10) for _ in range(10**6)]), A([r.choice([10, -10]) for _ in range(10**6)])],
            3: [A([r.choice([B, -B]) for _ in range(10**6)]), A([r.randint(-B, B) for _ in range(10**6)]), A([B] * (5 * 10**5) + [-B] * (5 * 10**5)),
                A([r.randint(-2, 2) * B for _ in range(10**6)])]}
def small(r):
    n = r.randint(1, 60); m = r.choice([1, 3, 10, 10**9])
    return A([r.randint(-m, m) for _ in range(n)])
