#include <cstdio>
#include <vector>
using namespace std;

int main() {
    if (fopen("UOCTANG.INP", "r")) {
        freopen("UOCTANG.INP", "r", stdin);
        freopen("UOCTANG.OUT", "w", stdout);
    }
    long long n; int q;
    scanf("%lld %d", &n, &q);
    vector<long long> ds;
    for (long long d = 1; d <= n; d++)           // tự động tăng dần
        if (n % d == 0) ds.push_back(d);
    printf("%d\n", (int)ds.size());
    for (size_t i = 0; i < ds.size(); i++)
        printf("%lld%c", ds[i], i + 1 == ds.size() ? '\n' : ' ');
    while (q--) {
        long long x, ans = -1;
        scanf("%lld", &x);
        for (long long d : ds)
            if (d >= x) { ans = d; break; }      // ước đầu tiên >= x
        printf("%lld\n", ans);
    }
    return 0;
}
