import sys
d = sys.stdin.read().split()
out = []
for i in range(int(d[0])):
    a1, p1, a2, p2 = map(int, d[1 + 4 * i:5 + 4 * i])
    s1 = set(range(a1, a1 + 3000 * p1, p1))
    t = a2; ans = -1
    for _ in range(3000):
        if t in s1: ans = t; break
        t += p2
    out.append(str(ans))
print('\n'.join(out))
