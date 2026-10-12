#include <iostream>
#include <string>
using namespace std;
typedef long long ll;

ll power(ll a, ll b, ll m) {                    // a < m, b nhỏ
    ll r = 1 % m;
    while (b > 0) {
        if (b & 1) r = r * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return r;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    if (fopen("SOMULON.INP", "r")) {
        freopen("SOMULON.INP", "r", stdin);
        freopen("SOMULON.OUT", "w", stdout);
    }
    int T;
    cin >> T;
    while (T--) {
        ll a, m;
        string b;
        cin >> a >> b >> m;
        a %= m;                                 // m <= 10^9: tích < 10^18
        ll pw[10];                              // pw[d] = a^d mod m
        pw[0] = 1 % m;
        for (int d = 1; d < 10; d++) pw[d] = pw[d - 1] * a % m;
        ll r = 1 % m;                       // r = a^(phần đầu đã đọc của b)
        for (char c : b)
            r = power(r, 10, m) * pw[c - '0'] % m;  // a^(10x + d)
        cout << r << '\n';
    }
    return 0;
}
