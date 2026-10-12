#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;
const int MOD = 1000000007, S = 4000;

int main() {
    if (fopen("CHIAKEO.INP", "r")) {
        freopen("CHIAKEO.INP", "r", stdin);
        freopen("CHIAKEO.OUT", "w", stdout);
    }
    vector<vector<int>> C(S, vector<int>(S, 0));    // 64 MB
    for (int a = 0; a < S; a++) {
        C[a][0] = 1;
        for (int b = 1; b <= a; b++)
            C[a][b] = (C[a - 1][b - 1] + C[a - 1][b]) % MOD;
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll n, k, t;
        scanf("%lld %lld %lld", &n, &k, &t);
        if (k * t > n) { printf("0\n"); continue; }
        printf("%d\n", C[n - k * t + k - 1][k - 1]);
    }
    return 0;
}
