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
    if (fopen("NTDOAN.INP", "r")) {
        freopen("NTDOAN.INP", "r", stdin);
        freopen("NTDOAN.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        ll L, R, c = 0, s = 0;
        scanf("%lld %lld", &L, &R);
        for (ll x = L; x <= R; x++)
            if (isPrime(x)) { c++; s += x; }
        printf("%lld %lld\n", c, s);
    }
    return 0;
}
