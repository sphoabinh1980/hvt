def samples():
    return [('3\n', '1\n5\n6\n25\n76\n376\n625\n')]
def tests():
    return {1: ['%d\n' % k for k in range(1, 8)], 2: ['%d\n' % k for k in (15, 17, 18)]}
def small(r):
    return '%d\n' % r.randint(1, 5)
