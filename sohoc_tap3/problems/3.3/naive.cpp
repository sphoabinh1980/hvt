#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;
const ll LIM = 1000000000000000000LL, INF = LIM + 1;    // INF: "vượt 10^18"

ll gcd(ll a, ll b) { while (b) { ll r = a % b; a = b; b = r; } return a; }
ll lcm(ll a, ll b) {                    // BCNN, chặn trên bởi INF
    if (a == INF || b == INF) return INF;
    ll x = a / gcd(a, b);
    if (x > LIM / b) return INF;        // x * b > 10^18
    return x * b;
}

int main() {
    if (fopen("DENNHAY.INP", "r")) {
        freopen("DENNHAY.INP", "r", stdin);
        freopen("DENNHAY.OUT", "w", stdout);
    }
    int n, q;
    scanf("%d %d", &n, &q);
    vector<ll> t(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &t[i]);
    while (q--) {
        int l, r;
        scanf("%d %d", &l, &r);
        ll v = 1;
        for (int i = l; i <= r && v != INF; i++) v = lcm(v, t[i]);
        printf("%lld\n", v == INF ? -1LL : v);
    }
    return 0;
}
