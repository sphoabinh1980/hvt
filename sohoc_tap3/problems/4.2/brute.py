import sys, math
d = sys.stdin.read().split()
out = []
for i in range(int(d[0])):
    a, b, c = map(int, d[1 + 3 * i:4 + 3 * i])
    g = math.gcd(a, b)
    if c % g: out.append('0'); continue
    a2, b2, c2 = a // g, b // g, c // g
    x = c2 * pow(a2, -1, b2) % b2 if b2 > 1 else 0
    out.append(str((c2 - a2 * x) // (a2 * b2) + 1 if a2 * x <= c2 else 0))
print('\n'.join(out))
