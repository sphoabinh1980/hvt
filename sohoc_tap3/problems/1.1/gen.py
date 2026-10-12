import random

def fmt(qs):
    return '%d\n' % len(qs) + ''.join('%d %d\n' % x for x in qs)

def samples():
    return [(fmt([(2, 1000), (2, -100), (2, 10**18)]), '8\n7\n3\n'),
            (fmt([(8, 0), (5, -7)]), '8\n5\n')]

def tests():
    r = random.Random(11)
    T = {1: [], 2: [], 3: []}
    T[1].append(fmt([(r.randint(2, 8), r.randint(0, 20)) for _ in range(10)]))
    T[1].append(fmt([(r.randint(2, 8), r.randint(0, 10**6)) for _ in range(1000)]))
    T[1].append(fmt([(r.randint(2, 8), r.randint(0, 10**6)) for _ in range(10**5)]))
    T[1].append(fmt([(r.randint(2, 8), 10**6 - r.randint(0, 6)) for _ in range(10**5)]))
    T[2].append(fmt([(r.randint(2, 8), r.randint(0, 10**18)) for _ in range(10**5)]))
    T[2].append(fmt([(r.randint(2, 8), 10**18 - r.randint(0, 100)) for _ in range(10**5)]))
    T[2].append(fmt([(8, 7 * r.randint(0, 10**17)) for _ in range(1000)]))
    T[3].append(fmt([(r.randint(2, 8), r.randint(-10**18, 10**18)) for _ in range(10**5)]))
    T[3].append(fmt([(r.randint(2, 8), -r.randint(0, 10**18)) for _ in range(10**5)]))
    T[3].append(fmt([(r.randint(2, 8), r.choice([-10**18, 10**18, -1, 0, 1, -7, -6, -13])) for _ in range(10**5)]))
    T[3].append(fmt([(r.randint(2, 8), r.randint(-30, 30)) for _ in range(1000)]))
    return T

def small(r):
    return fmt([(r.randint(2, 8), r.randint(-50, 50)) for _ in range(r.randint(1, 20))])
