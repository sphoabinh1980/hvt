#include <cstdio>
#include <vector>
using namespace std;

const int MAXN = 10000000;
int s[MAXN + 1];                                // 40 MB, toàn cục

int main() {
    if (fopen("BANBE.INP", "r")) {
        freopen("BANBE.INP", "r", stdin);
        freopen("BANBE.OUT", "w", stdout);
    }
    int N, k;
    scanf("%d %d", &N, &k);
    for (int d = 1; 2 * d <= N; d++)            // d là ước thực sự của
        for (int j = 2 * d; j <= N; j += d)     // 2d, 3d, 4d, ...
            s[j] += d;
    vector<pair<int, int>> res;
    for (int a = 1; a <= N; a++) {
        long long b = (long long)s[a] - k;      // có thể âm hoặc > N
        if (b > a && b <= N && s[b] == (long long)a + k)
            res.push_back({a, (int)b});
    }
    printf("%d\n", (int)res.size());
    for (auto& p : res) printf("%d %d\n", p.first, p.second);
    return 0;
}
