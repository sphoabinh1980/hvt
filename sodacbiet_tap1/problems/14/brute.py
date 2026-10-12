import sys
from itertools import combinations
d = sys.stdin.read().split(); s, k = d[0], int(d[1])
L = len(s); best = None
for keep in combinations(range(L), L - k):
    t = ''.join(s[i] for i in keep).lstrip('0') or '0'
    if best is None or (len(t), t) < (len(best), best): best = t
print(best)
