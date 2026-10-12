#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;

ll power(ll a, ll b, ll m) {
    ll r = 1 % m; a %= m;
    while (b) { if (b & 1) r = r * a % m; a = a * a % m; b >>= 1; }
    return r;
}

struct Prime {                            // dữ liệu cho một ước nguyên tố p
    ll p;
    vector<ll> f, inv;                // giai thừa, nghịch đảo giai thừa < p
    void init(ll pp) {
        p = pp; f.assign(p, 1); inv.assign(p, 1);
        for (ll i = 1; i < p; i++) f[i] = f[i - 1] * i % p;
        inv[p - 1] = power(f[p - 1], p - 2, p);
        for (ll i = p - 1; i > 0; i--) inv[i - 1] = inv[i] * i % p;
    }
    ll small(ll n, ll k) {                  // C(n, k) mod p với n, k < p
        if (k > n) return 0;
        return f[n] * inv[k] % p * inv[n - k] % p;
    }
    ll lucas(ll n, ll k) {           // tích C(n_i, k_i) theo chữ số cơ số p
        ll r = 1;
        while ((n > 0 || k > 0) && r) {
            r = r * small(n % p, k % p) % p;
            n /= p; k /= p;
        }
        return r;
    }
};

int main() {
    if (fopen("TOHOPLON.INP", "r")) {
        freopen("TOHOPLON.INP", "r", stdin);
        freopen("TOHOPLON.OUT", "w", stdout);
    }
    int q; ll m;
    scanf("%d %lld", &q, &m);
    Prime P;
    P.init(m);                              // coi m là số nguyên tố
    while (q--) {
        ll n, k;
        scanf("%lld %lld", &n, &k);
        printf("%lld\n", k > n ? 0 : P.lucas(n, k));
    }
    return 0;
}
