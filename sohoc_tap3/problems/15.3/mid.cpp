#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;
typedef vector<vector<ll>> Mat;
int n;

Mat mul(const Mat &a, const Mat &b) {
    Mat c(n, vector<ll>(n, 0));
    for (int i = 0; i < n; i++)
        for (int t = 0; t < n; t++)
            for (int j = 0; j < n; j++)       // lấy dư sau mỗi phép cộng
                c[i][j] = (c[i][j] + a[i][t] * b[t][j]) % MOD;
    return c;
}

int main() {
    if (fopen("DUONGK.INP", "r")) {
        freopen("DUONGK.INP", "r", stdin);
        freopen("DUONGK.OUT", "w", stdout);
    }
    int m, q;
    scanf("%d %d %d", &n, &m, &q);
    Mat A(n, vector<ll>(n, 0));
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        A[u - 1][v - 1] = 1;
    }
    while (q--) {
        int s, t; ll K;
        scanf("%d %d %lld", &s, &t, &K);
        Mat R(n, vector<ll>(n, 0)), B = A;
        for (int i = 0; i < n; i++) R[i][i] = 1;
        for (; K > 0; K >>= 1, B = mul(B, B)) // mỗi câu hỏi: ~120 phép nhân
            if (K & 1) R = mul(R, B);
        printf("%lld\n", R[s - 1][t - 1]);
    }
    return 0;
}
