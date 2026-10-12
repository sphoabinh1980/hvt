import sys
from sympy import primerange
L, R = map(int, sys.stdin.read().split())
ps = list(primerange(L, R + 1))
if len(ps) < 2: print(-1)
else:
    gs = [(ps[i + 1] - ps[i], i) for i in range(len(ps) - 1)]
    mx = max(g for g, i in gs); mn = min(g for g, i in gs)
    i1 = next(i for g, i in gs if g == mx); i2 = next(i for g, i in gs if g == mn)
    print(ps[i1], ps[i1 + 1]); print(ps[i2], ps[i2 + 1])
