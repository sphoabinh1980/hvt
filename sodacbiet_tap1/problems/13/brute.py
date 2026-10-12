import sys
from itertools import permutations
n = sys.stdin.read().split()[0]
best = None
for p in set(permutations(n)):
    s = ''.join(p)
    if s[0] != '0' and int(s) > int(n) and (best is None or int(s) < best): best = int(s)
print(best if best is not None else -1)
