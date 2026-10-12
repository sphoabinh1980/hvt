#include <cstdio>
typedef long long ll;
typedef __int128 LL;

int main() {
    if (fopen("PTDONGDU.INP", "r")) {
        freopen("PTDONGDU.INP", "r", stdin);
        freopen("PTDONGDU.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll a, c, m, L, R, cnt = 0, first = 0;
        scanf("%lld %lld %lld %lld %lld", &a, &c, &m, &L, &R);
        for (ll x = L; x <= R; x++)
            if (((LL)a * x - c) % m == 0) {     // m chia hết a·x − c
                if (cnt == 0) first = x;
                cnt++;
            }
        if (cnt == 0) printf("0\n");
        else printf("%lld %lld\n", cnt, first);
    }
    return 0;
}
