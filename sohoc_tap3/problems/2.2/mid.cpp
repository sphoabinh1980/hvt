#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    if (fopen("UOCTANG.INP", "r")) {
        freopen("UOCTANG.INP", "r", stdin);
        freopen("UOCTANG.OUT", "w", stdout);
    }
    long long n; int q;
    scanf("%lld %d", &n, &q);
    vector<long long> ds;
    for (long long d = 1; d * d <= n; d++)
        if (n % d == 0) {
            ds.push_back(d);
            if (d * d != n) ds.push_back(n / d);
        }
    sort(ds.begin(), ds.end());
    printf("%d\n", (int)ds.size());
    for (size_t i = 0; i < ds.size(); i++)
        printf("%lld%c", ds[i], i + 1 == ds.size() ? '\n' : ' ');
    while (q--) {
        long long x, ans = -1;
        scanf("%lld", &x);
        for (long long d : ds)                   // tới 6720 bước mỗi khách
            if (d >= x) { ans = d; break; }
        printf("%lld\n", ans);
    }
    return 0;
}
