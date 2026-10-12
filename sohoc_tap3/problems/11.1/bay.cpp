#include <cstdio>
typedef long long ll;

ll phi(ll n) {
    ll res = n;
    if (n % 2 == 0) {
        res -= res / 2;                     // nhân với (1 − 1/2)
        while (n % 2 == 0) n /= 2;
    }
    for (ll p = 3; p * p <= n; p += 2)      // chỉ thử số lẻ
        if (n % p == 0) {
            res -= res / p;                 // nhân với (1 − 1/p), chia hết
            while (n % p == 0) n /= p;
        }
    // quên: phần còn lại n > 1 là một ước nguyên tố lớn
    return res;
}

int main() {
    if (fopen("PHI.INP", "r")) {
        freopen("PHI.INP", "r", stdin);
        freopen("PHI.OUT", "w", stdout);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        ll n;
        scanf("%lld", &n);
        printf("%lld\n", phi(n));
    }
    return 0;
}
