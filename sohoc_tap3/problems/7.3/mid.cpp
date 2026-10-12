#include <cstdio>
#include <vector>
#include <map>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;

vector<pair<int, int>> factor(int x) {      // thử chia tới √x
    vector<pair<int, int>> f;
    for (int p = 2; p * p <= x; p++)
        if (x % p == 0) {
            int e = 0;
            while (x % p == 0) { x /= p; e++; }
            f.push_back({p, e});
        }
    if (x > 1) f.push_back({x, 1});
    return f;
}

int main() {
    if (fopen("BCNNDAY.INP", "r")) {
        freopen("BCNNDAY.INP", "r", stdin);
        freopen("BCNNDAY.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    vector<vector<pair<int, int>>> f(n);
    map<int, int> M;                        // số mũ lớn nhất của mỗi p
    for (int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        f[i] = factor(x);
        for (auto& pe : f[i]) M[pe.first] = max(M[pe.first], pe.second);
    }
    ll L = 1;
    for (auto& pe : M)
        for (int k = 0; k < pe.second; k++) L = L * pe.first % MOD;
    int need = 0;
    for (int i = 0; i < n; i++) {     // xóa thử a[i]: tính lại M không có i
        bool smaller = false;
        for (auto& pe : f[i]) {
            if (pe.second < M[pe.first]) continue;
            int best = 0;
            for (int j = 0; j < n; j++) if (j != i)
                for (auto& q : f[j])
                    if (q.first == pe.first) best = max(best, q.second);
            if (best < pe.second) smaller = true;
        }
        if (smaller) need++;
    }
    printf("%lld\n%d\n", L, need);
    return 0;
}
