#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("BAUOC.INP", "r")) {
        freopen("BAUOC.INP", "r", stdin);
        freopen("BAUOC.OUT", "w", stdout);
    }
    const int L = 10000;                        // (10^4)^3 = 10^12
    vector<bool> comp(L + 1, false);
    vector<int> pr;
    for (int i = 2; i <= L; i++)
        if (!comp[i]) {
            pr.push_back(i);                    // 1229 số nguyên tố <= 10^4
            for (int j = 2 * i; j <= L; j += i) comp[j] = true;
        }
    int n;
    scanf("%d", &n);
    while (n--) {
        ll r;
        scanf("%lld", &r);
        int cnt = 0;
        for (int p : pr) {                      // bóc mọi thừa số <= 10^4
            if (r % p) continue;
            int e = 0;
            while (r % p == 0) { r /= p; e++; }
            if (e >= 2) cnt++;
        }
        // r = 1, q, q^2 hoặc q*q' với q, q' > 10^4 nguyên tố
        if (r > 1) {
            ll s = (ll)sqrtl((long double)r);
            while (s * s > r) s--;
            while ((s + 1) * (s + 1) <= r) s++;
            if (s * s == r) cnt++;              // r = q^2
        }
        printf("%d\n", cnt);
    }
    return 0;
}
