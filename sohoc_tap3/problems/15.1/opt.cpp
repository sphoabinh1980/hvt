#include <cstdio>
typedef long long ll;
const ll MOD = 1000000007;

struct Mat { ll a[2][2]; };

Mat mul(const Mat &x, const Mat &y) {
    Mat z;
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)       // tổng hai tích < 2,1 * 10^18
            z.a[i][j] = (x.a[i][0] * y.a[0][j]
                       + x.a[i][1] * y.a[1][j]) % MOD;
    return z;
}

Mat power(Mat b, ll e) {
    Mat r = {{{1, 0}, {0, 1}}};          // ma trận đơn vị
    for (; e > 0; e >>= 1, b = mul(b, b))
        if (e & 1) r = mul(r, b);
    return r;
}

int main() {
    if (fopen("LATGACH.INP", "r")) {
        freopen("LATGACH.INP", "r", stdin);
        freopen("LATGACH.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    const Mat Q = {{{1, 1}, {1, 0}}};
    while (q--) {
        ll n;
        scanf("%lld", &n);
        Mat R = power(Q, n);       // Q^n = [[F(n+1), F(n)], [F(n), F(n-1)]]
        printf("%lld\n", R.a[0][0]);      // T(n) = F(n+1)
    }
    return 0;
}
