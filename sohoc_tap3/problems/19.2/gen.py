import random
def A(k, a): return '%d %d\n%s\n' % (len(a), k, ' '.join(map(str, a)))
def samples():
    return [(A(3, [2, -7, 5, 4, -3, 1]), '5 2\n'), (A(5, [1, 1, 1]), '0\n'), (A(6, [-1, 2, 7, -9, 5, -2]), '3 2\n')]
def tests():
    r = random.Random(192)
    B = 10**9
    return {1: [A(r.randint(1, 10**6), [r.randint(-B, B) for _ in range(3000)]), A(999983, [r.randint(-B, B) for _ in range(3000)]), A(7, [-1] * 3000), A(1, [5, -3])],
            2: [A(10**6, [r.randint(0, B) for _ in range(10**6)]), A(999983, [r.randint(0, 10) for _ in range(10**6)]), A(10**6, [1] * 999999 + [0]), A(2, [1] * 10**6)],
            3: [A(10**6, [r.randint(-B, B) for _ in range(10**6)]), A(999983, [r.randint(-B, B) for _ in range(10**6)]), A(13, [r.randint(-B, -1) for _ in range(10**6)]),
                A(10**6, [-1] * 10**6), A(1, [r.randint(-B, B) for _ in range(10**6)])]}
def small(r):
    n = r.randint(1, 40)
    return A(r.randint(1, 12), [r.randint(-20, 20) for _ in range(n)])
