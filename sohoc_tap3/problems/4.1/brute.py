import sys, math
d = sys.stdin.read().split()
n, q = int(d[0]), int(d[1])
g = 0
for x in d[2:2 + n]: g = math.gcd(g, int(x))
out = [str(g)] + ['CO' if int(c) % g == 0 else 'KHONG' for c in d[2 + n:2 + n + q]]
print('\n'.join(out))
