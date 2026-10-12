#include <cstdio>
typedef long long ll;
typedef unsigned int ui;

const int N = 10000000;
ui inv[N + 1];                          // p < 2^31: vừa unsigned int, 40 MB

int main() {
    if (fopen("NGHICHDAO.INP", "r")) {
        freopen("NGHICHDAO.INP", "r", stdin);
        freopen("NGHICHDAO.OUT", "w", stdout);
    }
    ll n, p;
    scanf("%lld %lld", &n, &p);
    inv[1] = 1;
    ll H = 1, X = 1;
    for (ll i = 2; i <= n; i++) {
        // p = q·i + r  =>  inv(i) = -q · inv(r) = (p - q) · inv(r)  (mod p)
        inv[i] = (ui)((p - p / i) * inv[p % i] % p);   // tích < 4·10^18
        H += inv[i];
        if (H >= p) H -= p;
        X ^= inv[i];
    }
    printf("%lld\n%lld\n", H, X);
    return 0;
}
