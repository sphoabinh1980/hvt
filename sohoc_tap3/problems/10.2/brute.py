import sys
n, p = map(int, sys.stdin.read().split())
H, X = 0, 0
for i in range(1, n + 1):
    v = pow(i, -1, p); H += v; X ^= v
print(H % p); print(X)
