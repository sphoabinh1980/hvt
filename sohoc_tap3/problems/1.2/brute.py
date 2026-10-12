import sys
sys.set_int_max_str_digits(0)
d = sys.stdin.read().split()
T = int(d[0])
print('\n'.join(str(pow(int(d[1 + 2 * i]), int(d[2 + 2 * i]), 10)) for i in range(T)))
