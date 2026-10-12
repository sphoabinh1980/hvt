#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("LUYTHUALON.INP", "r")) {
        freopen("LUYTHUALON.INP", "r", stdin);
        freopen("LUYTHUALON.OUT", "w", stdout);
    }
    ll a, b;
    scanf("%lld %lld", &a, &b);
    vector<ll> d(1, 1);               // d[0] là hàng đơn vị, mỗi ô 1 chữ số
    for (ll k = 0; k < b; k++) {
        ll c = 0;
        for (size_t i = 0; i < d.size(); i++) {
            ll t = d[i] * a + c;
            d[i] = t % 10;
            c = t / 10;
        }
        while (c > 0) { d.push_back(c % 10); c /= 10; }
        while (d.size() > 1 && d.back() == 0) d.pop_back();   // a = 0
    }
    for (int i = (int)d.size() - 1; i >= 0; i--) printf("%lld", d[i]);
    printf("\n");
    return 0;
}
