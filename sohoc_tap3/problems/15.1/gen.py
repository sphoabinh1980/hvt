import random
def fmt(a): return '%d\n' % len(a) + ''.join('%d\n' % x for x in a)
def samples():
    return [(fmt([1, 2, 4]), '1\n2\n5\n'), (fmt([10, 10**18]), '89\n680057396\n')]
def tests():
    r = random.Random(151)
    return {1: [fmt([r.randint(1, 20) for _ in range(1000)]), fmt(list(range(1, 21)))],
            2: [fmt([r.randint(1, 10**6) for _ in range(1000)]), fmt([10**6] * 1000)],
            3: [fmt([r.randint(1, 10**18) for _ in range(1000)]), fmt([10**18 - r.randint(0, 10**6) for _ in range(1000)]), fmt([2 * 10**9 + 15] * 10 + [10**18])]}
def small(r):
    return fmt([r.randint(1, 300) for _ in range(30)])
