import sys
sys.set_int_max_str_digits(0)
d = sys.stdin.read().split()
print('\n'.join(str(pow(int(d[1 + 3 * i]), int(d[2 + 3 * i]), int(d[3 + 3 * i]))) for i in range(int(d[0]))))
