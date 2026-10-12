#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("PHANSO.INP", "r")) {
        freopen("PHANSO.INP", "r", stdin);
        freopen("PHANSO.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    vector<int> L(q), R(q);
    int mx = 1;
    for (int i = 0; i < q; i++) {          // đọc hết câu hỏi để biết max R
        scanf("%d %d", &L[i], &R[i]);
        mx = max(mx, R[i]);
    }
    vector<int> phi(mx + 1);
    for (int i = 0; i <= mx; i++) phi[i] = i;
    for (int p = 2; p <= mx; p++)
        if (phi[p] == p)                    // p chưa bị đụng tới: nguyên tố
            for (int j = p; j <= mx; j += p) phi[j] -= phi[j] / p;
    vector<ll> S(mx + 1, 0);                    // tới ≈ 3·10^13: long long
    for (int b = 2; b <= mx; b++) S[b] = S[b - 1] + phi[b];   // b = 1 góp 0
    for (int i = 0; i < q; i++) printf("%lld\n", S[R[i]] - S[L[i] - 1]);
    return 0;
}
