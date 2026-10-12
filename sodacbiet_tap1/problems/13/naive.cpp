#include <bits/stdc++.h>
using namespace std;

string sorted_(long long x) {             // các chữ số của x, sắp tăng dần
    string s = to_string(x);
    sort(s.begin(), s.end());
    return s;
}

int main() {
    if (fopen("KETIEP.INP", "r")) {
        freopen("KETIEP.INP", "r", stdin);
        freopen("KETIEP.OUT", "w", stdout);
    }
    long long n;
    cin >> n;                           // chỉ dùng được khi n vừa long long
    string key = sorted_(n);                // tập chữ số của n (đã sắp xếp)
    long long lim = 1;
    while (lim <= n) lim *= 10;            // 10^(số chữ số): không vượt quá
    for (long long x = n + 1; x < lim; x++)
        if (sorted_(x) == key) { cout << x << "\n"; return 0; }
    cout << -1 << "\n";
    return 0;
}
