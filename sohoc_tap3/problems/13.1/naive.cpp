#include <cstdio>
typedef long long ll;
const ll MOD = 1000000007;
int k, t;

ll go(int i, int left) {                 // chia "left" kẹo cho các bạn i..k
    if (i == k) return left == 0 ? 1 : 0;
    ll s = 0;
    for (int x = t; x <= left; x++)         // bạn i nhận x >= t cái
        s += go(i + 1, left - x);
    return s % MOD;
}

int main() {
    if (fopen("CHIAKEO.INP", "r")) {
        freopen("CHIAKEO.INP", "r", stdin);
        freopen("CHIAKEO.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        int n;
        scanf("%d %d %d", &n, &k, &t);
        printf("%lld\n", go(0, n));
    }
    return 0;
}
