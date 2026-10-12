CODE = 'HAIDEN'
TL, ML = 1, 256
SUBTASKS = [30, 30, 40]
SOLS = [('naive.cpp', 'Mô phỏng hai dãy thời điểm nháy'),
        ('nogate.cpp', 'Gộp đồng dư, quên điều kiện "đã bật"'),
        ('opt.cpp', 'Gộp đồng dư tổng quát + số đầu tiên ≥ max(a₁, a₂)')]
REF = 'opt.cpp'
BRUTE = ['brute.py', 'brute2.py']
