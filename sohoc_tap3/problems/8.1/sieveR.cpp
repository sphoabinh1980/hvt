#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("NTDOAN.INP", "r")) {
        freopen("NTDOAN.INP", "r", stdin);
        freopen("NTDOAN.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        ll L, R, c = 0, s = 0;
        scanf("%lld %lld", &L, &R);
        vector<char> comp(R + 1, 0);      // R tới 10^12: không cấp phát nổi
        comp[0] = 1; if (R >= 1) comp[1] = 1;
        for (ll p = 2; p * p <= R; p++)
            if (!comp[p])
                for (ll j = p * p; j <= R; j += p) comp[j] = 1;
        for (ll x = L; x <= R; x++)
            if (!comp[x]) { c++; s += x; }
        printf("%lld %lld\n", c, s);
    }
    return 0;
}
