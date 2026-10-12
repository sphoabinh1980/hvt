#include <bits/stdc++.h>
using namespace std;

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
        long long c2 = 0, c5 = 0, rest = 1;     // n! = 2^c2 * 5^c5 * rest
        for (long long i = 2; i <= n; i++) {
            long long x = i;
            while (x % 2 == 0) { x /= 2; c2++; }
            while (x % 5 == 0) { x /= 5; c5++; }
            rest = rest * x % 10;               // phần không chứa 2, 5
        }
        // mỗi cặp (2, 5) tạo một số 0; còn dư c2 - c5 thừa số 2
        long long d = rest;
        for (long long k = 0; k < c2 - c5; k++) d = d * 2 % 10;
        cout << c5 << " " << d << "\n";
    }
    return 0;
}
