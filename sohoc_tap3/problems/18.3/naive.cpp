#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;
const int N = 100000;                    // chỉ đúng khi mọi số <= 10^5

int cnt[61][N + 1];                       // cnt[k][x]: số y <= x có k bit 1
vector<int> lst[61];                  // lst[k]: các số có k bit 1, tăng dần

int main() {
    if (fopen("KBIT.INP", "r")) {
        freopen("KBIT.INP", "r", stdin);
        freopen("KBIT.OUT", "w", stdout);
    }
    for (int x = 0; x <= N; x++) {
        int p = __builtin_popcount(x);
        for (int k = 0; k <= 60; k++)
            cnt[k][x] = (x ? cnt[k][x - 1] : 0) + (k == p);
        if (x > 0) lst[p].push_back(x);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        int type;
        scanf("%d", &type);
        if (type == 1) {
            ll L, R; int k;
            scanf("%lld %lld %d", &L, &R, &k);
            printf("%d\n", cnt[k][R] - (L ? cnt[k][L - 1] : 0));
        } else {
            int k; ll m;
            scanf("%d %lld", &k, &m);
            printf("%d\n", lst[k][m - 1]);
        }
    }
    return 0;
}
