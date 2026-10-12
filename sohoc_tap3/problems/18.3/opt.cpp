#include <cstdio>
typedef long long ll;

ll C[62][62];                           // C[60][30] ~ 1,18e17 vừa long long

// g(n) = số x trong [0, n] có đúng k bit 1
ll g(ll n, int k) {
    if (n < 0) return 0;
    ll s = 0; int t = 0;                 // t = số bit 1 của n đã đi qua
    for (int i = 60; i >= 0; i--)
        if (n >> i & 1) {
            // giống n ở các bit cao hơn i, bit i = 0, i bit thấp tùy ý
            if (k - t >= 0 && k - t <= i) s += C[i][k - t];
            t++;
        }
    if (t == k) s++;                      // chính n
    return s;
}

// số nguyên dương nhỏ thứ m có đúng k bit 1 (k >= 1)
ll kth(int k, ll m) {
    ll x = 0;
    for (int i = 59; i >= 0; i--) {
        ll zero = (k <= i) ? C[i][k] : 0;   // số cách nếu bit i = 0
        if (k > 0 && m > zero) {            // phải bật bit i
            x |= 1LL << i;
            m -= zero;
            k--;
        }
    }
    return x;
}

int main() {
    if (fopen("KBIT.INP", "r")) {
        freopen("KBIT.INP", "r", stdin);
        freopen("KBIT.OUT", "w", stdout);
    }
    for (int i = 0; i < 62; i++) {        // tam giác Pascal
        C[i][0] = 1;
        for (int j = 1; j <= i; j++)
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        int type;
        scanf("%d", &type);
        if (type == 1) {
            ll L, R; int k;
            scanf("%lld %lld %d", &L, &R, &k);
            printf("%lld\n", g(R, k) - g(L - 1, k));
        } else {
            int k; ll m;
            scanf("%d %lld", &k, &m);
            printf("%lld\n", kth(k, m));
        }
    }
    return 0;
}
