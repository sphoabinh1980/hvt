#include <cstdio>
#include <vector>
using namespace std;

long long gcd(long long a, long long b) {
    while (b) { long long r = a % b; a = b; b = r; }
    return a;
}

int main() {
    if (fopen("BOMOTSO.INP", "r")) {
        freopen("BOMOTSO.INP", "r", stdin);
        freopen("BOMOTSO.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &a[i]);
    long long best = -1; int idx = 0;
    for (int i = 1; i <= n; i++) {              // thử bỏ a[i]
        long long g = 0;
        for (int j = 1; j <= n; j++)
            if (j != i) g = gcd(g, a[j]);
        if (g > best) { best = g; idx = i; }    // > để giữ chỉ số nhỏ nhất
    }
    printf("%lld %d\n", best, idx);
    return 0;
}
