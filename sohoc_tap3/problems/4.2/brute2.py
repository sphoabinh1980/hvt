import sys
d = sys.stdin.read().split()
out = []
for i in range(int(d[0])):
    a, b, c = map(int, d[1 + 3 * i:4 + 3 * i])
    out.append(str(sum(1 for x in range(c // a + 1) if (c - a * x) % b == 0)))
print('\n'.join(out))
