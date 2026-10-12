#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;
const int N = 10000000;
int spf[N + 1];                             // ước nguyên tố nhỏ nhất
char M[N + 1];                              // M[p]: số mũ lớn nhất của p
int cnt[N + 1];                             // số phần tử đạt số mũ M[p]

int main() {
    if (fopen("BCNNDAY.INP", "r")) {
        freopen("BCNNDAY.INP", "r", stdin);
        freopen("BCNNDAY.OUT", "w", stdout);
    }
    int n;
    scanf("%d", &n);
    vector<int> a(n);
    int mx = 1;
    for (auto& x : a) { scanf("%d", &x); if (x > mx) mx = x; }
    for (ll p = 2; p <= mx; p++)            // sàng spf tới max(a)
        if (!spf[p]) {
            spf[p] = p;
            for (ll j = p * p; j <= mx; j += p) if (!spf[j]) spf[j] = p;
        }
    for (int x : a)                         // lượt 1: M[p] và cnt[p]
        while (x > 1) {
            int p = spf[x], e = 0;
            while (x % p == 0) { x /= p; e++; }
            if (e > M[p]) { M[p] = e; cnt[p] = 1; }
            else if (e == M[p]) cnt[p]++;
        }
    ll L = 1;
    for (int p = 2; p <= mx; p++)
        for (int k = 0; k < M[p]; k++) L = L * p % MOD;
    int need = 0;
    for (int x : a) {                  // lượt 2: a[i] có "độc quyền" p nào?
        bool ok = false;
        while (x > 1) {
            int p = spf[x], e = 0;
            while (x % p == 0) { x /= p; e++; }
            if (e == M[p] && cnt[p] == 1) ok = true;
        }
        need += ok;
    }
    printf("%lld\n%d\n", L, need);
    return 0;
}
