#include <bits/stdc++.h>
using namespace std;

const int SMALL[5] = {1, 1, 2, 6, 4};       // chữ số khác 0 cuối của 0!..4!
const int POW2[4] = {6, 2, 4, 8};     // 2^k mod 10 với k >= 1, theo k mod 4

int lastNonZero(long long n) {             // D(n) = 2^k * D(k) * D(n mod 5)
    if (n < 5) return SMALL[n];
    long long k = n / 5;
    return POW2[k % 4] * lastNonZero(k) * SMALL[n % 5] % 10;
}

long long trailingZeros(long long n) {       // Legendre: n/5 + n/25 + ...
    long long z = 0;
    while (n > 0) { n /= 5; z += n; }
    return z;
}

int main() {
    if (fopen("GIAITHUA.INP", "r")) {
        freopen("GIAITHUA.INP", "r", stdin);
        freopen("GIAITHUA.OUT", "w", stdout);
    }
    int Q;
    cin >> Q;
    while (Q--) {
        long long n;
        cin >> n;
        cout << trailingZeros(n) << " " << lastNonZero(n) << "\n";
    }
    return 0;
}
