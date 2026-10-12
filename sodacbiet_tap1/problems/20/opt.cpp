#include <bits/stdc++.h>
using namespace std;

int main() {
    if (fopen("HAMMING.INP", "r")) {
        freopen("HAMMING.INP", "r", stdin);
        freopen("HAMMING.OUT", "w", stdout);
    }
    int n;
    cin >> n;
    vector<long long> h(n);
    h[0] = 1;
    int i2 = 0, i3 = 0, i5 = 0;             // ba con trỏ
    for (int k = 1; k < n; k++) {
        long long a = h[i2] * 2, b = h[i3] * 3, c = h[i5] * 5;
        h[k] = min({a, b, c});              // ứng viên nhỏ nhất
        if (h[k] == a) i2++;                // tăng mọi con trỏ cho ra h[k]
        if (h[k] == b) i3++;                // để không sinh trùng
        if (h[k] == c) i5++;
    }
    cout << h[n - 1] << "\n";
    return 0;
}
