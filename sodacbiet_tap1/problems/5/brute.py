import sys
d = sys.stdin.read().split()
S, m, q = d[0], int(d[1]), int(d[2])
out = []
for i in range(q):
    l, r = int(d[3 + 2 * i]), int(d[4 + 2 * i])
    out.append(str(int(S[l - 1:r]) % m))
print('\n'.join(out))
