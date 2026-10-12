import sys, glob, os, re
# Rút khoảng trắng trước chú thích // để mọi dòng <= 76 kí tự
for pid in sys.argv[1:]:
    for f in glob.glob(os.path.join(os.path.dirname(__file__), '..', 'problems', pid, '*.cpp')):
        lines = open(f, encoding='utf-8').read().split('\n')
        out = []
        for l in lines:
            if len(l) > 76 and '//' in l:
                i = l.index('//')
                code = l[:i].rstrip()
                need = len(l) - 76
                gap = i - len(code)
                gap2 = max(1, gap - need)
                l = code + ' ' * gap2 + l[i:]
            if len(l) > 76:
                print('STILL LONG', f, len(l), l)
            out.append(l)
        open(f, 'w', encoding='utf-8').write('\n'.join(out))
