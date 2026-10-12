#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("TOHOPLON.INP", "r")) {
        freopen("TOHOPLON.INP", "r", stdin);
        freopen("TOHOPLON.OUT", "w", stdout);
    }
    int q; ll m;
    scanf("%d %lld", &q, &m);
    const int S = 2001;                     // chỉ dùng được khi n <= 2000
    vector<vector<ll>> C(S, vector<ll>(S, 0));
    for (int a = 0; a < S; a++) {
        C[a][0] = 1 % m;
        for (int b = 1; b <= a; b++)
            C[a][b] = (C[a - 1][b - 1] + C[a - 1][b]) % m;
    }
    while (q--) {
        ll n, k;
        scanf("%lld %lld", &n, &k);
        printf("%lld\n", k > n ? 0 : C[n][k]);
    }
    return 0;
}
