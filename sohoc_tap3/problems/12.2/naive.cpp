#include <cstdio>
typedef long long ll;

int main() {
    if (fopen("HAIDEN.INP", "r")) {
        freopen("HAIDEN.INP", "r", stdin);
        freopen("HAIDEN.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll a1, p1, a2, p2;
        scanf("%lld %lld %lld %lld", &a1, &p1, &a2, &p2);
        ll t1 = a1, t2 = a2, ans = -1;
        // sau mốc max(a1, a2) + p1·p2 thì mọi thứ đã lặp lại
        ll lim = (a1 > a2 ? a1 : a2) + p1 * p2;
        while (t1 <= lim && t2 <= lim) {
            if (t1 == t2) { ans = t1; break; }
            if (t1 < t2) t1 += p1;          // tiến đèn đang "chậm" hơn
            else t2 += p2;
        }
        printf("%lld\n", ans);
    }
    return 0;
}
