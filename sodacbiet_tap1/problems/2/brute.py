import sys
from decimal import Decimal, getcontext
getcontext().prec = 80
d = list(map(int, sys.stdin.read().split()))
out = []
for i in range(d[0]):
    a, b = d[1 + 2 * i], d[2 + 2 * i]
    x = Decimal(b) * Decimal(a).log10()
    fr = x - int(x)
    first = int(Decimal(10) ** (fr + 2))
    out.append('%d %03d' % (first, pow(a, b, 1000)))
print('\n'.join(out))
