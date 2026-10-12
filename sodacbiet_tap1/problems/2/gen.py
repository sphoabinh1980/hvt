import random, math
def ok(a, b): return b * math.log10(a) >= 6.0001
def fmt(q): return '%d\n' % len(q) + ''.join('%d %d\n' % x for x in q)
def samples():
    return [(fmt([(2, 100), (10, 6), (123456789, 1000000000)]), '126 376\n100 000\n147 001\n')]
def tests():
    r = random.Random(2)
    def rq(A, B):
        while True:
            a, b = r.randint(2, A), r.randint(1, B)
            if ok(a, b): return (a, b)
    return {1: [fmt([rq(1000, 2000) for _ in range(10)])], 2: [fmt([rq(10**9, 10**9) for _ in range(1000)]), fmt([(10**9, 10**9), (2, 10**9), (999999999, 999999999), (10, 10**9), (1000, 7)] * 3)]}
def small(r):
    q = []
    while len(q) < 20:
        a, b = r.randint(2, 10**9), r.randint(1, 10**9)
        if r.random() < 0.3: a = r.randint(2, 50)
        if ok(a, b): q.append((a, b))
    return fmt(q)
