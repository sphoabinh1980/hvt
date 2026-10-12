CODE = 'TONGDU'
TL, ML = 1, 256
SUBTASKS = [30, 30, 40]
SOLS = [('naive.cpp', 'Cộng trực tiếp n mod i, i = 1..k'),
        ('trap.cpp', 'Chia khối tới k, quên trường hợp i > n'),
        ('opt.cpp', 'n · k − Σ i · ⌊n/i⌋, chia khối trên [1, min(n, k)]')]
REF = 'opt.cpp'
BRUTE = 'brute.py'
