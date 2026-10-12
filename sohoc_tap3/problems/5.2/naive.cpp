#include <cstdio>
#include <vector>
using namespace std;

int main() {
    if (fopen("GOLDBACH.INP", "r")) {
        freopen("GOLDBACH.INP", "r", stdin);
        freopen("GOLDBACH.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        long long n;
        scanf("%lld", &n);
        vector<bool> comp(n + 1, false);    // sàng tới n: chỉ khi n nhỏ
        comp[0] = comp[1] = true;
        for (long long i = 2; i * i <= n; i++)
            if (!comp[i])
                for (long long j = i * i; j <= n; j += i) comp[j] = true;
        long long ans = -1;
        for (long long p = 2; p <= n / 2; p++)
            if (!comp[p] && !comp[n - p]) { ans = p; break; }
        if (ans < 0) printf("-1\n");
        else printf("%lld %lld\n", ans, n - ans);
    }
    return 0;
}
