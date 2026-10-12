// Miller–Rabin tất định cho mọi n < 3,3 * 10^24 (đủ cho long long)
bool isPrime(ll n) {
    if (n < 2) return false;
    for (ll p : {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37})
        if (n % p == 0) return n == p;
    ll d = n - 1; int s = 0;
    while (d % 2 == 0) { d /= 2; s++; }  // n - 1 = d * 2^s, d lẻ
    for (ll a : {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}) {
        ll x = power(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool comp = true;
        for (int i = 1; i < s && comp; i++) {
            x = mulmod(x, x, n);
            if (x == n - 1) comp = false;
        }
        if (comp) return false;
    }
    return true;
}
