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
        long long z = 0, last = 1;
        for (long long i = 2; i <= n; i++) {
            last *= i;
            while (last % 10 == 0) { last /= 10; z++; }  // bỏ số 0 tận cùng
            last %= 10;               // SAI: chỉ giữ một chữ số cuối
        }
        cout << z << " " << last << "\n";
    }
    return 0;
}
