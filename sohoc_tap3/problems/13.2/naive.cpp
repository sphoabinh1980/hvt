#include <cstdio>
#include <vector>
using namespace std;
const int MOD = 1000000007;

int main() {
    if (fopen("DUONGLUOI.INP", "r")) {
        freopen("DUONGLUOI.INP", "r", stdin);
        freopen("DUONGLUOI.OUT", "w", stdout);
    }
    int m, n, K;
    scanf("%d %d %d", &m, &n, &K);
    vector<vector<int>> f(m + 1, vector<int>(n + 1, 0));    // (m+1)(n+1) ô
    vector<vector<bool>> bad(m + 1, vector<bool>(n + 1, false));
    for (int i = 0; i < K; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        bad[x][y] = true;
    }
    for (int x = 0; x <= m; x++)
        for (int y = 0; y <= n; y++) {
            if (bad[x][y]) continue;            // f = 0 tại ô cấm
            if (x == 0 && y == 0) { f[x][y] = 1; continue; }
            int s = 0;
            if (x > 0) s = f[x - 1][y];
            if (y > 0) s = (s + f[x][y - 1]) % MOD;
            f[x][y] = s;
        }
    printf("%d\n", f[m][n]);
    return 0;
}
