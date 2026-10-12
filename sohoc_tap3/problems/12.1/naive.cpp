#include <cstdio>
typedef long long ll;

int main() {
    if (fopen("DIEMBINH.INP", "r")) {
        freopen("DIEMBINH.INP", "r", stdin);
        freopen("DIEMBINH.OUT", "w", stdout);
    }
    int k; ll L;
    scanf("%d %lld", &k, &L);
    ll m[10], a[10];
    for (int i = 0; i < k; i++) scanf("%lld %lld", &m[i], &a[i]);
    for (ll x = L; ; x++) {                     // thử từng số từ L trở lên
        bool ok = true;
        for (int i = 0; i < k && ok; i++)
            if (x % m[i] != a[i]) ok = false;
        if (ok) { printf("%lld\n", x); break; }
    }
    return 0;
}
