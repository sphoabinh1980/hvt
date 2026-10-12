import sys
from math import comb
d = sys.stdin.read().split()
out = []
for i in range(int(d[0])):
    n, k, t = map(int, d[1 + 3 * i:4 + 3 * i])
    out.append(str(comb(n - k * t + k - 1, k - 1) % (10**9 + 7) if n >= k * t else 0))
print('\n'.join(out))
