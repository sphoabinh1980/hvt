#include <cstdio>
#include <vector>
#include <set>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("CANCHI.INP", "r")) {
        freopen("CANCHI.INP", "r", stdin);
        freopen("CANCHI.OUT", "w", stdout);
    }
    int k, Q;
    scanf("%d %d", &k, &Q);
    vector<ll> m(k);
    for (auto& x : m) scanf("%lld", &x);
    ll P = 1;
    for (ll x : m) P *= x;                      // sau P năm thì tên lặp lại
    set<vector<ll>> names;                     // liệt kê tên của năm 0..P-1
    for (ll x = 0; x < P; x++) {
        vector<ll> nm(k);
        for (int i = 0; i < k; i++) nm[i] = x % m[i];
        names.insert(nm);
    }
    printf("%d\n", (int)names.size());
    while (Q--) {
        vector<ll> c(k);
        ll L, R, cnt = 0, first = -1;
        for (auto& x : c) scanf("%lld", &x);
        scanf("%lld %lld", &L, &R);
        for (ll x = L; x <= R; x++) {           // thử từng năm
            bool ok = true;
            for (int i = 0; i < k && ok; i++)
                if (x % m[i] != c[i]) ok = false;
            if (ok) { if (first < 0) first = x; cnt++; }
        }
        if (cnt == 0) printf("0\n");
        else printf("%lld %lld\n", cnt, first);
    }
    return 0;
}
