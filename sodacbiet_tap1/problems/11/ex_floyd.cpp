#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll f(ll x) {
    ll s = 0;
    for (; x > 0; x /= 10) s += (x % 10) * (x % 10);
    return s;
}

// Floyd ("rùa và thỏ"): tìm độ dài đuôi mu và chu trình lam, bộ nhớ O(1)
void floyd(ll x0, ll &mu, ll &lam) {
    ll t = f(x0), h = f(f(x0));          // rùa đi 1 bước, thỏ đi 2 bước
    while (t != h) { t = f(t); h = f(f(h)); }
    mu = 0; t = x0;                       // đặt rùa về đầu, cùng đi 1 bước
    while (t != h) { t = f(t); h = f(h); mu++; }
    lam = 1; h = f(t);                    // đi một vòng để đo chu trình
    while (t != h) { h = f(h); lam++; }
}

int main() {
    ll x, mu, lam;
    while (cin >> x) { floyd(x, mu, lam); cout << mu << " " << lam << "\n"; }
    return 0;
}
