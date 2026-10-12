#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

// mulmod, powmod, isPrime: Miller–Rabin như chương trình NTDX
ull mulmod(ull a, ull b, ull m) { return (unsigned __int128)a * b % m; }
ull powmod(ull a, ull e, ull m) {
    ull r = 1;
    for (a %= m; e > 0; e >>= 1, a = mulmod(a, a, m))
        if (e & 1) r = mulmod(r, a, m);
    return r;
}
bool isPrime(ull n) {
    if (n < 2) return false;
    for (ull p : {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37})
        if (n % p == 0) return n == p;
    ull d = n - 1; int s = 0;
    while (d % 2 == 0) d /= 2, s++;
    for (ull a : {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}) {
        ull x = powmod(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool comp = true;
        for (int i = 1; i < s && comp; i++)
            if ((x = mulmod(x, x, n)) == n - 1) comp = false;
        if (comp) return false;
    }
    return true;
}

vector<ull> res;
void grow(ull x) {                         // x đã là số nguyên tố cắt phải
    res.push_back(x);
    for (int d : {1, 3, 7, 9})             // chữ số cuối chẵn hay 5: hợp số
        if (isPrime(x * 10 + d)) grow(x * 10 + d);
}

int main() {
    for (int d : {2, 3, 5, 7}) grow(d);
    sort(res.begin(), res.end());
    cout << res.size() << " " << res.back() << "\n";
    return 0;
}
