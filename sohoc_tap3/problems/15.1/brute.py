import sys
d = list(map(int, sys.stdin.read().split()))
out = []
for n in d[1:]:
    # đếm trực tiếp: số cách lát = số dãy gồm các khối 1 (dọc) và 2 (hai ngang) có tổng n
    w = [1] + [0] * n
    for i in range(1, n + 1):
        w[i] = w[i - 1] + (w[i - 2] if i >= 2 else 0)
    out.append(str(w[n] % (10**9 + 7)))
print('\n'.join(out))
