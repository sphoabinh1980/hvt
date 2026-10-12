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
    vector<long long> a(n + 2), L(n + 2, 0), R(n + 2, 0);  // L[0]=R[n+1]=0
    for (int i = 1; i <= n; i++) scanf("%lld", &a[i]);
    for (int i = 1; i <= n; i++) L[i] = gcd(L[i - 1], a[i]);   // a[1..i]
    for (int i = n; i >= 1; i--) R[i] = gcd(R[i + 1], a[i]);   // a[i..n]
    long long best = -1; int idx = 0;
    for (int i = 1; i <= n; i++) {
        long long g = gcd(L[i - 1], R[i + 1]);  // bỏ a[i]
        if (g > best) { best = g; idx = i; }
    }
    printf("%lld %d\n", best, idx);
    return 0;
}
