#include <cstdio>
typedef long long ll;

int main() {
    if (fopen("BOISO.INP", "r")) {
        freopen("BOISO.INP", "r", stdin);
        freopen("BOISO.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll L, R, a, b, c, cnt = 0;
        scanf("%lld %lld %lld %lld %lld", &L, &R, &a, &b, &c);
        for (ll x = L; x <= R; x++)
            if ((x % a == 0 || x % b == 0) && x % c != 0) cnt++;
        printf("%lld\n", cnt);
    }
    return 0;
}
