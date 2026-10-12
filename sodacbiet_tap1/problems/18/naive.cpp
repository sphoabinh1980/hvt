#include <bits/stdc++.h>
using namespace std;

long long s(long long x) {                  // tổng các ước thực sự của x
    if (x == 1) return 0;
    long long r = 1;
    for (long long d = 2; d * d <= x; d++)
        if (x % d == 0) {
            r += d;
            if (d != x / d) r += x / d;
        }
    return r;
}

int main() {
    if (fopen("THANTHIET.INP", "r")) {
        freopen("THANTHIET.INP", "r", stdin);
        freopen("THANTHIET.OUT", "w", stdout);
    }
    long long N;
    cin >> N;
    vector<pair<long long, long long>> res;
    for (long long a = 1; a <= N; a++) {
        long long b = s(a);
        if (b > a && b <= N && s(b) == a) res.push_back({a, b});
    }
    cout << res.size() << "\n";
    for (auto [a, b] : res) cout << a << " " << b << "\n";
    return 0;
}
