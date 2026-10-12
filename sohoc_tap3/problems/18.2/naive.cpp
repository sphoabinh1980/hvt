#include <cstdio>
typedef long long ll;

int main() {
    if (fopen("BITDOAN.INP", "r")) {
        freopen("BITDOAN.INP", "r", stdin);
        freopen("BITDOAN.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll L, R, s = 0;
        scanf("%lld %lld", &L, &R);
        for (ll x = L; x <= R; x++) s += __builtin_popcountll(x);
        printf("%lld\n", s);
    }
    return 0;
}
