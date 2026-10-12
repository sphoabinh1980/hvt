#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;
const ll BASE = 1000000000;            // mỗi ô 9 chữ số

int main() {
    if (fopen("LUYTHUALON.INP", "r")) {
        freopen("LUYTHUALON.INP", "r", stdin);
        freopen("LUYTHUALON.OUT", "w", stdout);
    }
    ll a, b;
    scanf("%lld %lld", &a, &b);
    vector<ll> d(1, 1);                 // số lớn 1; d[0] là ô thấp nhất
    for (ll k = 0; k < b; k++) {
        ll c = 0;
        for (size_t i = 0; i < d.size(); i++) {
            ll t = d[i] * a + c;        // < 10^18 + 10^9: vừa long long
            d[i] = t % BASE;
            c = t / BASE;               // c < a <= 10^9
        }
        if (c > 0) d.push_back(c);      // thêm nhiều nhất một ô
        while (d.size() > 1 && d.back() == 0) d.pop_back();   // a = 0
    }
    printf("%lld", d.back());           // ô cao nhất: in bình thường
    for (int i = (int)d.size() - 2; i >= 0; i--)
        printf("%lld", d[i]);           // BẪY: thiếu các số 0 đầu ô
    printf("\n");
    return 0;
}
