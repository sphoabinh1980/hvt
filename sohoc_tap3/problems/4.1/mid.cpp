#include <cstdio>
#include <vector>
using namespace std;

long long gcd(long long a, long long b) {
    while (b) { long long r = a % b; a = b; b = r; }
    return a;
}

int main() {
    if (fopen("DONGNUOC.INP", "r")) {
        freopen("DONGNUOC.INP", "r", stdin);
        freopen("DONGNUOC.OUT", "w", stdout);
    }
    int n, q;
    scanf("%d %d", &n, &q);
    vector<long long> a(n);
    for (auto& x : a) scanf("%lld", &x);
    long long g = (n == 1) ? a[0] : gcd(a[0], a[1]);   // quên các can sau
    printf("%lld\n", g);
    while (q--) {
        long long c;
        scanf("%lld", &c);
        puts(c % g == 0 ? "CO" : "KHONG");
    }
    return 0;
}
