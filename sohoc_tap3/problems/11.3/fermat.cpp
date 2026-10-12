#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;

ll power(ll a, ll b, ll m) {
    a %= m; ll r = 1 % m;
    while (b) { if (b & 1) r = r * a % m; a = a * a % m; b >>= 1; }
    return r;
}

int main() {
    if (fopen("THAPLT.INP", "r")) {
        freopen("THAPLT.INP", "r", stdin);
        freopen("THAPLT.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        int k; ll m;
        scanf("%d %lld", &k, &m);
        vector<ll> a(k);
        for (auto& x : a) scanf("%lld", &x);
        // chỉ cho k = 3, m nguyên tố, m ∤ a1: số mũ rút gọn theo m − 1
        ll e = (m == 1) ? 0 : power(a[1], a[2], m - 1);
        printf("%lld\n", power(a[0], e, m));
    }
    return 0;
}
