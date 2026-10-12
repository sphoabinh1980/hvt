import sys
from sympy import factorint
d = sys.stdin.read().split()
out = []
for i in range(int(d[0])):
    n, b = int(d[1 + 2 * i]), int(d[2 + 2 * i])
    best = None
    for p, k in factorint(b).items():
        e, m = 0, n
        while m: m //= p; e += m
        best = e // k if best is None else min(best, e // k)
    out.append(str(best))
print('\n'.join(out))
