#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;
const int OFF = 10000000;               // |S| <= 10^6 * 10 = 10^7

int main() {
    if (fopen("TONG0.INP", "r")) {
        freopen("TONG0.INP", "r", stdin);
        freopen("TONG0.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    vector<int> cnt(2 * OFF + 1, 0);    // cnt[S + OFF]
    ll s = 0, ans = 0;
    cnt[OFF] = 1;                       // S0 = 0
    for (int i = 0; i < n; i++) {
        ll x;
        scanf("%lld", &x);
        s += x;
        ans += cnt[s + OFF];            // cặp với các tiền tố trước
        cnt[s + OFF]++;                 // chỉ đúng khi |a_i| <= 10
    }
    printf("%lld\n", ans);
    return 0;
}
