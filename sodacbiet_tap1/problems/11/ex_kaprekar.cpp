#include <bits/stdc++.h>
using namespace std;

int kap(int x) {                          // một bước Kaprekar với 4 chữ số
    int d[4];
    for (int i = 0; i < 4; i++) { d[i] = x % 10; x /= 10; }
    sort(d, d + 4);                       // tăng dần
    int lo = 0, hi = 0;
    for (int i = 0; i < 4; i++) { lo = lo * 10 + d[i]; hi = hi * 10 + d[3 - i]; }
    return hi - lo;
}

int main() {                              // số bước để về 6174, mọi số 4 chữ số
    int hist[10] = {0};
    for (int x = 1000; x <= 9999; x++) {
        if (x % 1111 == 0) continue;      // bốn chữ số giống nhau: bỏ
        int s = 0;
        for (int y = x; y != 6174; y = kap(y)) s++;
        hist[s]++;
    }
    for (int s = 0; s < 10; s++) if (hist[s]) cout << s << ": " << hist[s] << "\n";
    return 0;
}
