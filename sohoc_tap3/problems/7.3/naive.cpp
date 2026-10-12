#include <cstdio>
#include <vector>
using namespace std;
typedef __int128 LL;

LL gcd(LL a, LL b) { while (b) { LL r = a % b; a = b; b = r; } return a; }
// BCNN chính xác của dãy, bỏ qua phần tử skip
LL lcmAll(const vector<LL>& a, int skip) {
    LL v = 1;
    for (int i = 0; i < (int)a.size(); i++)
        if (i != skip) v = v / gcd(v, a[i]) * a[i];  // tràn khi > 1,7·10^38
    return v;
}

int main() {
    if (fopen("BCNNDAY.INP", "r")) {
        freopen("BCNNDAY.INP", "r", stdin);
        freopen("BCNNDAY.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    vector<LL> a(n);
    for (auto& x : a) { long long t; scanf("%lld", &t); x = t; }
    LL L = lcmAll(a, -1);
    int need = 0;
    for (int i = 0; i < n; i++)
        if (lcmAll(a, i) < L) need++;
    printf("%lld\n%d\n", (long long)(L % 1000000007), need);
    return 0;
}
