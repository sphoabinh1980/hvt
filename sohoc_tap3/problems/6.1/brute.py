import sys
d = sys.stdin.read().split()
q = int(d[0])
qs = [(int(d[1 + 2 * i]), int(d[2 + 2 * i])) for i in range(q)]
def isp(x):
    if x < 2: return False
    i = 2
    while i * i <= x:
        if x % i == 0: return False
        i += 1
    return True
out = []
for t, x in qs:
    if t == 1: out.append(str(sum(1 for v in range(2, x + 1) if isp(v))))
    else:
        c, v = 0, 1
        while c < x:
            v += 1
            if isp(v): c += 1
        out.append(str(v))
print('\n'.join(out))
