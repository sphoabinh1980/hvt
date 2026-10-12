import sys
from sympy import primerange
d = sys.stdin.read().split()
out = []
for i in range(int(d[0])):
    L, R = int(d[1 + 2 * i]), int(d[2 + 2 * i])
    ps = list(primerange(L, R + 1))
    out.append('%d %d' % (len(ps), sum(ps)))
print('\n'.join(out))
