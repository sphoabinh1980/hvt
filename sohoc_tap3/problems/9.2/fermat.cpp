#include <iostream>
#include <string>
using namespace std;
typedef long long ll;

ll power(ll a, ll b, ll m) {
    a %= m;
    ll r = 1 % m;
    while (b > 0) {
        if (b & 1) r = r * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return r;
}

int main() {
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
        if (m == 1) { cout << 0 << '\n'; continue; }
        ll e = 0;                               // e = b mod (m - 1)
        for (char c : b) e = (e * 10 + (c - '0')) % (m - 1);
        cout << power(a, e, m) << '\n';   // chỉ đúng khi m nguyên tố, m ∤ a
    }
    return 0;
}
