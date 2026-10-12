import sys
from math import comb
d = list(map(int, sys.stdin.read().split()))
q, m = d[0], d[1]
print('\n'.join(str(comb(d[2 + 2 * i], d[3 + 2 * i]) % m) for i in range(q)))
