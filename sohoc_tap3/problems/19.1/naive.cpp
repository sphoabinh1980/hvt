#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("TONG0.INP", "r")) {
        freopen("TONG0.INP", "r", stdin);
        freopen("TONG0.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    vector<ll> a(n);
    for (ll &x : a) scanf("%lld", &x);
    ll cnt = 0;
    for (int l = 0; l < n; l++) {
        ll s = 0;
        for (int r = l; r < n; r++) {
            s += a[r];                   // tổng đoạn [l, r]
            if (s == 0) cnt++;
        }
    }
    printf("%lld\n", cnt);
    return 0;
}
