#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

ll phi(ll n) {
    ll res = n;
    for (ll p = 2; p * p <= n; p++)
        if (n % p == 0) {
            res -= res / p;
            while (n % p == 0) n /= p;
        }
    if (n > 1) res -= res / n;
    return res;
}

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
    vector<ll> S(mx + 1, 0);                    // S[b] = φ(2) + ... + φ(b)
    for (int b = 2; b <= mx; b++) S[b] = S[b - 1] + phi(b);   // O(√b) mỗi b
    for (int i = 0; i < q; i++) printf("%lld\n", S[R[i]] - S[L[i] - 1]);
    return 0;
}
