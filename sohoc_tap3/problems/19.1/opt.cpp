#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("TONG0.INP", "r")) {
        freopen("TONG0.INP", "r", stdin);
        freopen("TONG0.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    vector<ll> S(n + 1, 0);             // S[0] = 0
    for (int i = 1; i <= n; i++) {
        ll x;
        scanf("%lld", &x);
        S[i] = S[i - 1] + x;            // |S| <= 10^15: long long
    }
    sort(S.begin(), S.end());
    ll ans = 0;
    for (int i = 0, j; i <= n; i = j) {
        j = i;
        while (j <= n && S[j] == S[i]) j++;   // nhóm [i, j) bằng nhau
        ll c = j - i;
        ans += c * (c - 1) / 2;
    }
    printf("%lld\n", ans);
    return 0;
}
