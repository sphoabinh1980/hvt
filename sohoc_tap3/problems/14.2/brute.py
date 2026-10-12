import sys
from sympy import primefactors
d = list(map(int, sys.stdin.read().split()))
out = []
for i in range(d[0]):
    n, N = d[1 + 2 * i], d[2 + 2 * i]
    ps = primefactors(n); tot = 0
    for mask in range(1 << len(ps)):
        prod, bits = 1, 0
        for j, p in enumerate(ps):
            if mask >> j & 1: prod *= p; bits += 1
        tot += (-1) ** bits * (N // prod)
    out.append(str(tot))
print('\n'.join(out))
