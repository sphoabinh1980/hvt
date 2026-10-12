CODE = 'TONGSIGMA'
TL, ML = 1, 256
SUBTASKS = [20, 30, 50]
SOLS = [('naive.cpp', 'Tính σ(x) cho từng x bằng duyệt ước tới √x'),
        ('mid.cpp', 'Đếm hai lần: Σ i · ⌊n/i⌋, i = 1..n'),
        ('trap.cpp', 'Chia khối, lấy dư i, j trước khi chia 2'),
        ('opt.cpp', 'Chia khối, tổng khối bằng __int128')]
REF = 'opt.cpp'
BRUTE = 'brute.py'
