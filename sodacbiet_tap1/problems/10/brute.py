import sys
K = int(sys.stdin.read())
for n in range(1, 10 ** K):
    s = str(n)
    if sum(int(c) ** len(s) for c in s) == n: print(n)
