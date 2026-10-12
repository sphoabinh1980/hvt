import sys
d = list(map(int, sys.stdin.read().split()))
out = []
for i in range(d[0]):
    L, R = d[1 + 2 * i], d[2 + 2 * i]
    out.append(str(sum(bin(x).count('1') for x in range(L, R + 1))))
print('\n'.join(out))
