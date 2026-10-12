#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("TONGCS.INP", "r")) {
        freopen("TONGCS.INP", "r", stdin);
        freopen("TONGCS.OUT", "w", stdout);
    }
    long long n;
    cin >> n;
    long long S = 0;
    for (long long x = 1; x <= n; x++) {   // xét từng số x
        long long y = x;
        while (y > 0) {                     // tách từng chữ số của x
            S += y % 10;                    // chữ số hàng đơn vị
            y /= 10;                        // bỏ chữ số hàng đơn vị
        }
    }
    cout << S << "\n";
    return 0;
}
