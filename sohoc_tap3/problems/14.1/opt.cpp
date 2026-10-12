#include <cstdio>
typedef long long ll;
const ll LIM = 1000000000000000000LL, INF = 2 * LIM;    // INF: "vượt 10^18"

ll gcd(ll a, ll b) { while (b) { ll r = a % b; a = b; b = r; } return a; }
ll lcm(ll a, ll b) {                    // chặn trên: > 10^18 thì trả INF
    if (a >= INF || b >= INF) return INF;
    ll x = a / gcd(a, b);
    if (x > LIM / b) return INF;
    return x * b;
}
ll a, b, c, AB, AC, BC, ABC;
ll f(ll N) {                            // số x trong [1, N] thỏa mãn đề
    if (N <= 0) return 0;
    ll AorB = N / a + N / b - N / AB;               // |A ∪ B|
    ll AorBandC = N / AC + N / BC - N / ABC;        // |(A ∪ B) ∩ C|
    return AorB - AorBandC;
}

int main() {
    if (fopen("BOISO.INP", "r")) {
        freopen("BOISO.INP", "r", stdin);
        freopen("BOISO.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll L, R;
        scanf("%lld %lld %lld %lld %lld", &L, &R, &a, &b, &c);
        AB = lcm(a, b); AC = lcm(a, c); BC = lcm(b, c); ABC = lcm(AB, c);
        printf("%lld\n", f(R) - f(L - 1));
    }
    return 0;
}
