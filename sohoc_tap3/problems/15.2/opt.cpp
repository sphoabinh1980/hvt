#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;

struct Mat { ll a[3][3]; };

Mat mul(const Mat &x, const Mat &y) {
    Mat z;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++) {
            ll s = 0;
            for (int t = 0; t < 3; t++)
                s = (s + x.a[i][t] * y.a[t][j]) % MOD;
            z.a[i][j] = s;
        }
    return z;
}

// v <- T^e * v, với v = (f[x], f[x-1], f[x-2])
void advance(ll v[3], ll e) {
    Mat b = {{{1, 1, 1}, {1, 0, 0}, {0, 1, 0}}};    // ma trận đồng hành
    Mat r = {{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}};
    for (; e > 0; e >>= 1, b = mul(b, b))
        if (e & 1) r = mul(r, b);
    ll w[3];
    for (int i = 0; i < 3; i++)
        w[i] = (r.a[i][0] * v[0] % MOD + r.a[i][1] * v[1] % MOD
                + r.a[i][2] * v[2] % MOD) % MOD;
    for (int i = 0; i < 3; i++) v[i] = w[i];
}

int main() {
    if (fopen("TRIBO.INP", "r")) {
        freopen("TRIBO.INP", "r", stdin);
        freopen("TRIBO.OUT", "w", stdout);
    }
    ll n; int K;
    scanf("%lld %d", &n, &K);
    vector<ll> b(K);
    for (ll &x : b) scanf("%lld", &x);
    sort(b.begin(), b.end());             // bậc hỏng cho không theo thứ tự
    ll v[3] = {1, 0, 0};                  // (f[0], f[-1], f[-2])
    ll cur = 0;
    for (ll x : b) {
        advance(v, x - cur);              // đi từ bậc cur lên bậc x
        v[0] = 0;                         // bậc x hỏng: f[x] = 0
        cur = x;
    }
    advance(v, n - cur);
    printf("%lld\n", v[0]);
    return 0;
}
