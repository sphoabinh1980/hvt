import sys
D = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = sys.stdin.read().split()
out = []
for i in range(int(d[0])):
    a, b, s = int(d[1 + 3 * i]), int(d[2 + 3 * i]), d[3 + 3 * i]
    v = int(s, a); r = ''
    while True:
        r = D[v % b] + r; v //= b
        if v == 0: break
    out.append(r)
print('\n'.join(out))
