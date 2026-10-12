import sys
n, k = map(int, sys.stdin.read().split())
print(sum(n % i for i in range(1, k + 1)) % (10**9 + 7))
