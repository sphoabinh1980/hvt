ll gcd(ll a, ll b) {                     // a, b >= 0; gcd(0, 0) = 0
    while (b) { ll r = a % b; a = b; b = r; }
    return a;
}

// lcm có chặn: trả về INF nếu lcm(a, b) > LIM (tránh tràn khi nhân)
const ll LIM = 1000000000000000000LL, INF = 2 * LIM;
ll lcmCap(ll a, ll b) {
    if (a >= INF || b >= INF) return INF;
    ll x = a / gcd(a, b);                 // chia trước, nhân sau
    if (x > LIM / b) return INF;
    return x * b;
}

// Euclid mở rộng: trả về g = gcd(a, b) và x, y với a x + b y = g
ll extgcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1, g = extgcd(b, a % b, x1, y1);
    x = y1; y = x1 - (a / b) * y1;
    return g;
}

// nghịch đảo của a theo mô-đun m; trả về -1 nếu gcd(a, m) != 1
ll inverse(ll a, ll m) {
    ll x, y, g = extgcd(md(a, m), m, x, y);
    return g != 1 ? -1 : md(x, m);
}
