import sys, math
d = sys.stdin.read().split()
out = []
for i in range(int(d[0])):
    n, b = int(d[1 + 2 * i]), int(d[2 + 2 * i])
    f = math.factorial(n); c = 0
    while f % b == 0: f //= b; c += 1
    out.append(str(c))
print('\n'.join(out))
