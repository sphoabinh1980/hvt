int main() {
    printf("%lld %lld %lld\n", md(-7, 3), power(2, 1000000006, 1000000007), mulmod(999999999999999989LL, 999999999999999989LL, 1000000000000000003LL));
    printf("%lld %lld %lld\n", gcd(12, 18), lcmCap(1000000000LL, 999999999LL), lcmCap(LIM, 3));
    ll x, y; ll g = extgcd(240, 46, x, y); printf("%lld %lld %lld %lld\n", g, x, y, 240 * x + 46 * y);
    printf("%lld %lld\n", inverse(3, 7), inverse(4, 8));
    ll r, m; bool ok = crt(2, 3, 3, 5, r, m); printf("%d %lld %lld\n", ok, r, m);
    ok = crt(1, 4, 3, 6, r, m); printf("%d %lld %lld\n", ok, r, m);
    ok = crt(1, 4, 2, 6, r, m); printf("%d\n", ok);
    sieve(1000000); printf("%zu\n", pr.size());
    auto f = factorSmall(360); for (auto p : f) printf("%d^%d ", p.first, p.second); printf("\n");
    auto F = factorBig(200560490130LL); printf("%zu ", F.size()); auto G = factorBig(999999999989LL); printf("%lld\n", G[0].first);
    printf("%d %d %d\n", isPrime(1000000000000000003LL), isPrime(1000000007LL * 998244353LL), isPrime(2));
    initComb(2000000); printf("%lld %lld\n", C(12, 2), C(2000000, 1000000));
    Mat Q = {{1, 1}, {1, 0}}; Mat R = matPow(Q, 10); printf("%lld\n", R[0][0]);
    print128((lll)-1000000000000000000LL * 1000000000000000000LL); printf("\n");
    return 0;
}
