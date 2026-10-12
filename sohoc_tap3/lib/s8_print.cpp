#include <cstdio>
// in số __int128 (có thể âm): printf và cout không làm được
void print128(lll x) {
    if (x < 0) { putchar('-'); x = -x; }
    char buf[45]; int len = 0;
    do { buf[len++] = '0' + (int)(x % 10); x /= 10; } while (x > 0);
    while (len > 0) putchar(buf[--len]);
}
