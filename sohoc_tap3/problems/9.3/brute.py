import sys
d = sys.stdin.read().split()
out = []
for i in range(int(d[0])):
    a, n, m = int(d[1 + 3 * i]), int(d[2 + 3 * i]), int(d[3 + 3 * i])
    s, p = 0, 1
    for _ in range(n + 1): s += p; p = p * a % m
    out.append(str(s % m))
print('\n'.join(out))
