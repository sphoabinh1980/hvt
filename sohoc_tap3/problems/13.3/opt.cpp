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
    vector<Prime> P;
    vector<ll> coef;                        // hệ số ghép Trung Hoa
    ll t = m;
    for (ll p = 2; p * p <= t; p++)
        if (t % p == 0) { P.push_back({}); P.back().init(p); t /= p; }
    if (t > 1) { P.push_back({}); P.back().init(t); }
    for (auto& pr : P) {                   // e ≡ 1 (mod p), e ≡ 0 (mod m/p)
        ll M = m / pr.p;
        coef.push_back(M % m * power(M % pr.p, pr.p - 2, pr.p) % m);
    }
    while (q--) {
        ll n, k;
        scanf("%lld %lld", &n, &k);
        ll x = 0;
        if (k <= n)
            for (size_t i = 0; i < P.size(); i++)   // tích < 10^5 · 10^10
                x = (x + P[i].lucas(n, k) * coef[i]) % m;
        printf("%lld\n", x % m);            // m = 1: luôn 0
    }
    return 0;
}
