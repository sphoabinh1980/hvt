import sys
d = sys.stdin.read().split()
q = int(d[0])
out = []
for i in range(q):
    t, k = int(d[1 + 2 * i]), int(d[2 + 2 * i])
    out.append(str((t - 2 + k) % 7 + 2))   # % của Python luôn không âm
print('\n'.join(out))
