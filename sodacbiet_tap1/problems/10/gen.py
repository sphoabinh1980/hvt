def samples():
    return [('3\n', '1\n2\n3\n4\n5\n6\n7\n8\n9\n153\n370\n371\n407\n')]
def tests():
    return {1: ['%d\n' % k for k in range(1, 8)], 2: ['%d\n' % k for k in (16, 17, 18)]}
def small(r):
    return '%d\n' % r.randint(1, 5)
