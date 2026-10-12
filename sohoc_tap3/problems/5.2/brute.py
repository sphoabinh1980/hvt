import sys
def isp(x):
    if x < 2: return False
    i = 2
    while i * i <= x:
        if x % i == 0: return False
        i += 1
    return True
d = sys.stdin.read().split()
out = []
for x in d[1:1 + int(d[0])]:
    n = int(x); res = '-1'
    for p in range(2, n // 2 + 1):
        if isp(p) and isp(n - p): res = '%d %d' % (p, n - p); break
    out.append(res)
print('\n'.join(out))
