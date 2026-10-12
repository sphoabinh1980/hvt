import sys
n = int(sys.stdin.read())
k = 1
while True:
    s = bin(k)[2:]
    if int(s) % n == 0:
        print(s); break
    k += 1
