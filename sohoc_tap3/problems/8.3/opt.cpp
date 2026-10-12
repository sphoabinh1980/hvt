#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("UOCDOAN.INP", "r")) {
        freopen("UOCDOAN.INP", "r", stdin);
        freopen("UOCDOAN.OUT", "w", stdout);
    }
    ll L, R;
    scanf("%lld %lld", &L, &R);
    const int S = 1000000;
    vector<char> comp(S + 1, 0);
    vector<int> pr;
    for (int i = 2; i <= S; i++)
        if (!comp[i]) {
            pr.push_back(i);
            for (ll j = (ll)i * i; j <= S; j += i) comp[j] = 1;
        }
    int n = R - L + 1;
    vector<ll> rest(n);                     // phần còn lại chưa phân tích
    vector<ll> d(n, 1);                     // số ước, nhân dần
    for (int i = 0; i < n; i++) rest[i] = L + i;
    for (int p : pr) {
        if ((ll)p * p > R) break;
        // duyệt MỌI bội của p trong đoạn (không lấy max với p²)
        for (ll j = (L + p - 1) / p * p; j <= R; j += p) {
            ll& x = rest[j - L];
            int e = 0;
            while (x % p == 0) { x /= p; e++; }
            d[j - L] *= (e + 1);
        }
    }
    ll sum = 0, best = L, bd = 0;
    for (int i = 0; i < n; i++) {
        if (rest[i] > 1) d[i] *= 2;      // phần còn lại là một số nguyên tố
        sum += d[i];
        if (d[i] > bd) { bd = d[i]; best = L + i; }
    }
    printf("%lld\n%lld %lld\n", sum, best, bd);
    return 0;
}
