#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("NTDOAN.INP", "r")) {
        freopen("NTDOAN.INP", "r", stdin);
        freopen("NTDOAN.OUT", "w", stdout);
    }
    const int S = 1000000;                  // √(10^12)
    vector<char> comp(S + 1, 0);
    vector<int> pr;                         // 78 498 số nguyên tố <= 10^6
    for (int i = 2; i <= S; i++)
        if (!comp[i]) {
            pr.push_back(i);
            for (ll j = (ll)i * i; j <= S; j += i) comp[j] = 1;
        }
    int T;
    scanf("%d", &T);
    while (T--) {
        ll L, R;
        scanf("%lld %lld", &L, &R);
        vector<char> mark(R - L + 1, 0);    // mark[x - L] = 1: x là hợp số
        for (int p : pr) {
            if ((ll)p * p > R) break;
            ll start = (L + p - 1) / p * p; // bội nhỏ nhất của p mà >= L
            if (start < (ll)p * p) start = (ll)p * p;  // không gạch chính p
            for (ll j = start; j <= R; j += p) mark[j - L] = 1;
        }
        if (L == 1) mark[0] = 1;            // số 1 không nguyên tố
        ll c = 0, s = 0;                    // tổng tới ≈ 3,6·10^16
        for (ll x = L; x <= R; x++)
            if (!mark[x - L]) { c++; s += x; }
        printf("%lld %lld\n", c, s);
    }
    return 0;
}
