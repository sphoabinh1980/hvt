import sys
d = list(map(int, sys.stdin.read().split()))
f = lambda x: sum(int(c) ** 2 for c in str(x))
out = []
for i in range(d[0]):
    x, K = d[1 + 2 * i], d[2 + 2 * i]
    for _ in range(K): x = f(x)
    out.append(str(x))
print('\n'.join(out))
