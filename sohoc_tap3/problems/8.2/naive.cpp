#include <cstdio>
typedef long long ll;

bool isPrime(ll x) {
    if (x < 2) return false;
    if (x < 4) return true;
    if (x % 2 == 0 || x % 3 == 0) return false;
    for (ll i = 5; i * i <= x; i += 6)
        if (x % i == 0 || x % (i + 2) == 0) return false;
    return true;
}

int main() {
    if (fopen("KHOANGCACH.INP", "r")) {
        freopen("KHOANGCACH.INP", "r", stdin);
        freopen("KHOANGCACH.OUT", "w", stdout);
    }
    ll L, R;
    scanf("%lld %lld", &L, &R);
    ll prev = -1, bmax = -1, pmax = 0, bmin = -1, pmin = 0;
    for (ll x = L; x <= R; x++) {
        if (!isPrime(x)) continue;
        if (prev > 0) {                     // cặp liên tiếp (prev, x)
            ll g = x - prev;
            // so sánh chặt (>, <) để khi hòa giữ cặp có p nhỏ nhất
            if (bmax < 0 || g > bmax) { bmax = g; pmax = prev; }
            if (bmin < 0 || g < bmin) { bmin = g; pmin = prev; }
        }
        prev = x;
    }
    if (bmax < 0) printf("-1\n");
    else {
        printf("%lld %lld\n", pmax, pmax + bmax);
        printf("%lld %lld\n", pmin, pmin + bmin);
    }
    return 0;
}
