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
    vector<long long> small, big;              // ước nhỏ tăng, ước lớn giảm
    for (long long d = 1; d * d <= n; d++)
        if (n % d == 0) {
            small.push_back(d);
            if (d * d != n) big.push_back(n / d);
        }
    vector<long long> ds = small;            // nối ước lớn theo chiều ngược
    for (int i = (int)big.size() - 1; i >= 0; i--) ds.push_back(big[i]);
    printf("%d\n", (int)ds.size());
    for (size_t i = 0; i < ds.size(); i++)
        printf("%lld%c", ds[i], i + 1 == ds.size() ? '\n' : ' ');
    while (q--) {
        long long x;
        scanf("%lld", &x);
        auto it = lower_bound(ds.begin(), ds.end(), x);  // phần tử đầu >= x
        printf("%lld\n", it == ds.end() ? -1LL : *it);
    }
    return 0;
}
