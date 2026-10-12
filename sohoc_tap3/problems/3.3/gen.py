import random
def fmt(t, qs):
    return '%d %d\n%s\n' % (len(t), len(qs), ' '.join(map(str, t))) + ''.join('%d %d\n' % x for x in qs)
def rq(r, n, Q, l1=False, longq=False):
    out = []
    for _ in range(Q):
        if l1:
            out.append((1, r.randint(1, n)))
        elif longq:
            a = r.randint(1, 50); b = r.randint(n - 50, n); out.append((a, b))
        else:
            a, b = sorted((r.randint(1, n), r.randint(1, n))); out.append((a, b))
    return out
def tvals(r, n, kind):
    if kind == 'small': return [r.choice([1, 2, 3, 4, 6, 12]) for _ in range(n)]
    if kind == 'pow': return [2 ** r.randint(0, 61) if r.random() < 0.5 else 1 for _ in range(n)]
    if kind == 'mix': return [r.choice([1, 2, 3, 5, 7, 2 ** r.randint(0, 20), r.randint(1, 10**6), r.randint(1, 10**18)]) for _ in range(n)]
    if kind == 'big': return [r.randint(1, 10**18) for _ in range(n)]
    if kind == 'one': return [1] * n
def samples():
    return [(fmt([2, 3, 4, 5], [(1, 3), (2, 2), (3, 4), (1, 4)]), '12\n3\n20\n60\n'),
            (fmt([10**9, 10**9, 999999999, 10**18], [(1, 2), (1, 3), (2, 4), (4, 4)]), '1000000000\n999999999000000000\n-1\n1000000000000000000\n')]
def tests():
    r = random.Random(33)
    T = {1: [], 2: [], 3: []}
    for k in ['small', 'pow', 'mix', 'big']:
        T[1].append(fmt(tvals(r, 2000, k), rq(r, 2000, 2000)))
    T[1].append(fmt(tvals(r, 2000, 'one'), rq(r, 2000, 2000, longq=True)))
    for k in ['small', 'pow', 'mix', 'one']:
        T[2].append(fmt(tvals(r, 200000, k), rq(r, 200000, 200000, l1=True)))
    for k in ['small', 'pow', 'mix', 'big', 'one']:
        T[3].append(fmt(tvals(r, 200000, k), rq(r, 200000, 200000, longq=(k in ('small', 'one')))))
    T[3].append(fmt(tvals(r, 200000, 'small'), rq(r, 200000, 200000)))
    return T
def small(r):
    n = r.randint(1, 12)
    t = [r.choice([1, 2, 3, 4, 6, 10**9, 999999999, 10**18, r.randint(1, 50), 2 ** r.randint(0, 60)]) for _ in range(n)]
    return fmt(t, rq(r, n, r.randint(1, 15)))
