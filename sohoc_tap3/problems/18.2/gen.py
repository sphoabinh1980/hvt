import random
def fmt(qs): return '%d\n' % len(qs) + ''.join('%d %d\n' % x for x in qs)
def rq(r, M):
    a, b = r.randint(1, M), r.randint(1, M); return (min(a, b), max(a, b))
def samples():
    return [(fmt([(1, 12), (5, 7)]), '22\n7\n'), (fmt([(1, 10**18), (10**18, 10**18)]), '29761222783429247000\n24\n')]
def tests():
    r = random.Random(182)
    return {1: [fmt([rq(r, 10**6) for _ in range(10)]), fmt([(1, 10**6), (10**6, 10**6), (1, 1)])],
            2: [fmt([rq(r, 10**17) for _ in range(10**5)]), fmt([(1, 10**17)] * 1000 + [(2**56 - 1, 10**17)])],
            3: [fmt([rq(r, 10**18) for _ in range(10**5)]), fmt([(1, 10**18)] * 10**4 + [(r.randint(1, 10**6), 10**18) for _ in range(1000)]), fmt([(2**59, 10**18), (1, 2**59 - 1)])]}
def small(r):
    return fmt([rq(r, 3000) for _ in range(20)])
