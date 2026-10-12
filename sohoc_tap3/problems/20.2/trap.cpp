#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;
typedef long long ll;

ll gcd(ll a, ll b) { while (b) { ll r = a % b; a = b; b = r; } return a; }

int main() {
    if (fopen("DAGIAC.INP", "r")) {
        freopen("DAGIAC.INP", "r", stdin);
        freopen("DAGIAC.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    vector<ll> x(n), y(n);
    for (int i = 0; i < n; i++) scanf("%lld %lld", &x[i], &y[i]);
    ll S2 = 0, B = 0;                     // S2 = 2 lần diện tích (có dấu)
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;              // cạnh cuối P_n -> P_1
        S2 += llabs(x[i] * y[j] - x[j] * y[i]);   // BẪY
        B += gcd(llabs(x[j] - x[i]), llabs(y[j] - y[i]));
    }
    ll I = (S2 - B + 2) / 2;              // định lí Pick
    printf("%lld %lld\n", I, B);
    return 0;
}
