import sys
n, m = map(int, sys.stdin.read().split())
print(sum((n % i) * (m % i) for i in range(1, min(n, m) + 1)) % (10**9 + 7))
