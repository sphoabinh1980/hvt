#include <cstdio>
typedef long long ll;

int main() {
    if (fopen("UOCDOAN.INP", "r")) {
        freopen("UOCDOAN.INP", "r", stdin);
        freopen("UOCDOAN.OUT", "w", stdout);
    }
    ll L, R;
    scanf("%lld %lld", &L, &R);
    ll sum = 0, best = L, bd = 0;
    for (ll x = L; x <= R; x++) {
        ll c = 0;
        for (ll k = 1; k * k <= x; k++)     // cặp ước, O(√x)
            if (x % k == 0) c += (k * k == x) ? 1 : 2;
        sum += c;
        if (c > bd) { bd = c; best = x; }
    }
    printf("%lld\n%lld %lld\n", sum, best, bd);
    return 0;
}
