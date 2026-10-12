#include <bits/stdc++.h>
using namespace std;

// Các phép tính cơ bản trên chữ số của n >= 0
int soChuSo(long long n) {
    int k = 0;
    do { k++; n /= 10; } while (n > 0);     // do-while: n = 0 có 1 chữ số
    return k;
}
int tongChuSo(long long n) {
    int s = 0;
    while (n > 0) { s += n % 10; n /= 10; }
    return s;
}
long long tichChuSo(long long n) {
    long long p = 1;
    do { p *= n % 10; n /= 10; } while (n > 0);
    return p;
}
long long daoNguoc(long long n) {            // 1200 -> 21
    long long r = 0;
    while (n > 0) { r = r * 10 + n % 10; n /= 10; }
    return r;
}

int main() {
    long long n;
    while (cin >> n)
        cout << soChuSo(n) << " " << tongChuSo(n) << " "
             << tichChuSo(n) << " " << daoNguoc(n) << "\n";
    return 0;
}
