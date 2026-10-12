#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

ull mulmod(ull a, ull b, ull m) { return (unsigned __int128)a * b % m; }

ull powmod(ull a, ull e, ull m) {
    ull r = 1;
    for (a %= m; e > 0; e >>= 1, a = mulmod(a, a, m))
        if (e & 1) r = mulmod(r, a, m);
    return r;
}

bool isPrime(ull n) {                       // Miller–Rabin tất định
    if (n < 2) return false;
    for (ull p : {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37})
        if (n % p == 0) return n == p;
    ull d = n - 1;
    int s = 0;
    while (d % 2 == 0) d /= 2, s++;
    for (ull a : {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}) {
        ull x = powmod(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool comp = true;
        for (int i = 1; i < s && comp; i++) {
            x = mulmod(x, x, n);
            if (x == n - 1) comp = false;
        }
        if (comp) return false;
    }
    return true;
}

int main() {
    if (fopen("NTDX.INP", "r")) {
        freopen("NTDX.INP", "r", stdin);
        freopen("NTDX.OUT", "w", stdout);
    }
    long long L, R;
    cin >> L >> R;
    long long cnt = (L <= 11 && 11 <= R);   // 11: số đối xứng chẵn duy nhất
    long long lo = 1;                     // nửa đầu có h chữ số: [lo, 10lo)
    for (int h = 1; h <= 7; h++, lo *= 10) {
        for (long long a = lo; a < lo * 10; a++) {
            int first = a / lo;             // chữ số đầu = chữ số cuối
            if (h > 1 && first % 2 == 0) { a += lo - 1; continue; }
            if (h > 1 && first == 5) { a += lo - 1; continue; }
            long long x = a;                // ghép độ dài lẻ: abc -> abcba
            for (long long y = a / 10; y > 0; y /= 10) x = x * 10 + y % 10;
            if (x > R) break;
            if (x >= L && isPrime(x)) cnt++;
        }
    }
    cout << cnt << "\n";
    return 0;
}
