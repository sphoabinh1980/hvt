#include <cstdio>
typedef long long ll;

// f(n) = popcount(0) + ... + popcount(n); tràn khi n gần 10^18
ll f(ll n) {
    ll s = 0;
    for (int k = 0; k <= 60; k++) {
        ll half = 1LL << k, period = half << 1;
        ll q = (n + 1) / period, r = (n + 1) % period;
        s += q * half + (r > half ? r - half : 0);
    }
    return s;
}

int main() {
    if (fopen("BITDOAN.INP", "r")) {
        freopen("BITDOAN.INP", "r", stdin);
        freopen("BITDOAN.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll L, R;
        scanf("%lld %lld", &L, &R);
        printf("%lld\n", f(R) - f(L - 1));
    }
    return 0;
}
