#include <cstdio>
#include <vector>
using namespace std;
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

vector<ll> lst[61];                       // loại 2: bảng tính sẵn tới 10^5

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
    for (ll x = 1; x <= 100000; x++)
        lst[__builtin_popcountll(x)].push_back(x);
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
            // chỉ đúng khi đáp số <= 10^5
            printf("%lld\n", m <= (ll)lst[k].size() ? lst[k][m - 1] : -1);
        }
    }
    return 0;
}
