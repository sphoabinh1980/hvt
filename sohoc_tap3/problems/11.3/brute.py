import sys
d = sys.stdin.read().split()
T = int(d[0]); p = 1
out = []
for _ in range(T):
    k, m = int(d[p]), int(d[p + 1]); a = list(map(int, d[p + 2:p + 2 + k])); p += 2 + k
    E = a[-1]
    for x in reversed(a[1:-1]):
        E = x ** E                      # giá trị thật của tháp con (nhỏ)
    out.append(str(pow(a[0], E, m) if k > 1 else a[0] % m))
print('\n'.join(out))
