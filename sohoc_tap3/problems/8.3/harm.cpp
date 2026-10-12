#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("UOCDOAN.INP", "r")) {
        freopen("UOCDOAN.INP", "r", stdin);
        freopen("UOCDOAN.OUT", "w", stdout);
    }
    ll L, R;
    scanf("%lld %lld", &L, &R);
    vector<int> d(R + 1, 0);                // chỉ dùng được khi R nhỏ
    for (ll k = 1; k <= R; k++)
        for (ll j = k; j <= R; j += k) d[j]++;
    ll sum = 0, best = L;
    for (ll x = L; x <= R; x++) {
        sum += d[x];
        if (d[x] > d[best]) best = x;
    }
    printf("%lld\n%lld %d\n", sum, best, d[best]);
    return 0;
}
