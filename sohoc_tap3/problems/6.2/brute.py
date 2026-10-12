import sys
d = sys.stdin.read().split()
q = int(d[0])
def isp(x):
    return x > 1 and all(x % i for i in range(2, int(x ** 0.5) + 1))
out = []
for i in range(q):
    a, b = int(d[1 + 2 * i]), int(d[2 + 2 * i])
    out.append(str(sum(1 for p in range(a, b - 1) if isp(p) and isp(p + 2))))
print('\n'.join(out))
