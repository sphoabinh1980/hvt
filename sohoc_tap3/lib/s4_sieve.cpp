#include <vector>
using namespace std;

// spf[i]: ước nguyên tố nhỏ nhất của i (2 <= i <= n); pr: các số nguyên tố
vector<int> spf, pr;
void sieve(int n) {
    spf.assign(n + 1, 0);
    for (int i = 2; i <= n; i++) {
        if (spf[i] == 0) { spf[i] = i; pr.push_back(i); }
        for (int p : pr) {                // sàng tuyến tính O(n)
            if (p > spf[i] || (ll)i * p > n) break;
            spf[i * p] = p;
        }
    }
}

// phân tích x <= n thành thừa số nguyên tố trong O(log x) nhờ spf
vector<pair<int, int>> factorSmall(int x) {
    vector<pair<int, int>> f;
    while (x > 1) {
        int p = spf[x], e = 0;
        while (x % p == 0) { x /= p; e++; }
        f.push_back({p, e});
    }
    return f;
}

// phân tích x <= 10^12 bằng các số nguyên tố p <= 10^6 trong pr
vector<pair<ll, int>> factorBig(ll x) {
    vector<pair<ll, int>> f;
    for (int p : pr) {
        if ((ll)p * p > x) break;
        if (x % p == 0) {
            int e = 0;
            while (x % p == 0) { x /= p; e++; }
            f.push_back({p, e});
        }
    }
    if (x > 1) f.push_back({x, 1});      // phần còn lại là số nguyên tố
    return f;
}
