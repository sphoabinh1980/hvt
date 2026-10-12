#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("BOI01.INP", "r")) {
        freopen("BOI01.INP", "r", stdin);
        freopen("BOI01.OUT", "w", stdout);
    }
    long long n;
    cin >> n;
    // các số chỉ gồm 0 và 1, theo thứ tự tăng: 1, 10, 11, 100, 101, ...
    // chính là biểu diễn nhị phân của k = 1, 2, 3, ... đọc như số thập phân
    for (unsigned long long k = 1;; k++) {
        long long r = 0;
        for (int b = 63 - __builtin_clzll(k); b >= 0; b--)
            r = (r * 10 + (k >> b & 1)) % n;          // số dư theo Horner
        if (r == 0) {
            for (int b = 63 - __builtin_clzll(k); b >= 0; b--)
                cout << (k >> b & 1);
            cout << "\n";
            return 0;
        }
    }
}
