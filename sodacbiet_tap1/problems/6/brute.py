import sys
def dr(x):
    while x >= 10: x = sum(map(int, str(x)))
    return x
d = list(map(int, sys.stdin.read().split()))
out = []
for i in range(d[0]):
    L, R, k = d[1 + 3 * i: 4 + 3 * i]
    out.append(str(sum(1 for x in range(L, R + 1) if dr(x) == k)))
print('\n'.join(out))
