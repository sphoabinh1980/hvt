#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<ll> primes;                            // số nguyên tố <= 10^6

ll mulmod(ll a, ll b, ll m) { return (ll)((__int128)a * b % m); }
ll power(ll a, ll b, ll m) {
    ll r = 1 % m;
    for (a %= m; b > 0; b >>= 1, a = mulmod(a, a, m))
        if (b & 1) r = mulmod(r, a, m);
    return r;
}
vector<ll> primeFactors(ll x) {               // các ước nguyên tố phân biệt
    vector<ll> f;
    for (ll p : primes) {
        if (p * p > x) break;
        if (x % p == 0) { f.push_back(p); while (x % p == 0) x /= p; }
    }
    if (x > 1) f.push_back(x);
    return f;
}

int main() {
    if (fopen("CHUKY.INP", "r")) {
        freopen("CHUKY.INP", "r", stdin);
        freopen("CHUKY.OUT", "w", stdout);
    }
    vector<bool> comp(1000001, false);
    for (ll i = 2; i <= 1000000; i++)
        if (!comp[i]) {
            primes.push_back(i);
            for (ll j = i * i; j <= 1000000; j += i) comp[j] = true;
        }
    int Q;
    cin >> Q;
    while (Q--) {
        ll n;
        cin >> n;
        int a = 0, b = 0;                     // n = 2^a * 5^b * m
        ll m = n;
        while (m % 2 == 0) { m /= 2; a++; }
        while (m % 5 == 0) { m /= 5; b++; }
        int pre = max(a, b);                  // độ dài phần không tuần hoàn
        if (m == 1) { cout << pre << " 0\n"; continue; }
        ll phi = m;                           // phi(m)
        for (ll p : primeFactors(m)) phi = phi / p * (p - 1);
        ll ord = phi;                         // cấp của 10 chia hết phi(m)
        for (ll p : primeFactors(phi))
            while (ord % p == 0 && power(10, ord / p, m) == 1) ord /= p;
        cout << pre << " " << ord << "\n";
    }
    return 0;
}
