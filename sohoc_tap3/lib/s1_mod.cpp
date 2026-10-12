typedef long long ll;
typedef unsigned long long ull;
typedef __int128 lll;

// số dư không âm của x khi chia cho m (m > 0), kể cả khi x < 0
ll md(ll x, ll m) { return (x % m + m) % m; }

// a * b mod m, an toàn với a, b, m tới 9,2 * 10^18
ll mulmod(ll a, ll b, ll m) { return (ll)((lll)a * b % m); }

// a^b mod m bằng lũy thừa nhanh; trả về 1 % m khi b = 0
ll power(ll a, ll b, ll m) {
    ll r = 1 % m;
    a = md(a, m);
    for (; b > 0; b >>= 1, a = mulmod(a, a, m))
        if (b & 1) r = mulmod(r, a, m);
    return r;
}
