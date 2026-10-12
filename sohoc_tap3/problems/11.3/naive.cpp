#include <cstdio>
#include <vector>
using namespace std;
typedef unsigned long long ull;
typedef unsigned __int128 u128;

ull ipow(ull a, ull e) {               // giá trị thật (đề bảo đảm <= 10^18)
    ull r = 1;
    for (ull i = 0; i < e; i++) r = (ull)((u128)r * a);
    return r;
}

int main() {
    if (fopen("THAPLT.INP", "r")) {
        freopen("THAPLT.INP", "r", stdin);
        freopen("THAPLT.OUT", "w", stdout);
    }
    int T;
    scanf("%d", &T);
    while (T--) {
        int k; ull m;
        scanf("%d %llu", &k, &m);
        vector<ull> a(k);
        for (auto& x : a) scanf("%llu", &x);
        ull v = a[k - 1];
        for (int i = k - 2; i >= 0; i--) {  // từ trên xuống
            if (a[i] <= 1) v = (a[i] == 1 || v == 0) ? 1 : 0;   // 1^v, 0^v
            else v = ipow(a[i], v);         // a >= 2: số mũ v nhỏ (<= 60)
        }
        printf("%llu\n", v % m);
    }
    return 0;
}
