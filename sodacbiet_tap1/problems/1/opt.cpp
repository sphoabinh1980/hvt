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
    for (long long p = 1; p <= n; p *= 10) { // p = 1, 10, 100, ...: một cột
        long long high = n / (p * 10);          // số chu kì trọn vẹn
        long long cur = n / p % 10;             // chữ số của n ở cột này
        long long low = n % p;                  // phần bên phải cột này
        S += high * 45 * p;                   // mỗi chu kì: (0+1+...+9) * p
        S += cur * (cur - 1) / 2 * p;   // chữ số 0..cur-1, mỗi số p lần
        S += cur * (low + 1);                  // chữ số cur lặp low + 1 lần
    }
    cout << S << "\n";
    return 0;
}
