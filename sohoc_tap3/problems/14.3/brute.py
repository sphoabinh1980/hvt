import sys
from math import comb
n, m = map(int, sys.stdin.read().split())
k = n - m
P = 10**9 + 7
D = [1, 0]
for i in range(2, k + 1): D.append((i - 1) * (D[-1] + D[-2]))
print(comb(n, k) * D[k] % P)
