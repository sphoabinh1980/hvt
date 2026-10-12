import sys
K = int(sys.stdin.read())
for n in range(1, 10 ** K):
    if (n * n - n) % (10 ** len(str(n))) == 0: print(n)
