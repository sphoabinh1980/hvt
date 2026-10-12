import sys
from sympy import divisor_count
L, R = map(int, sys.stdin.read().split())
ds = [int(divisor_count(x)) for x in range(L, R + 1)]
m = max(ds); i = ds.index(m)
print(sum(ds)); print(L + i, m)
