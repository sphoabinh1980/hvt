#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;

int main() {
    if (fopen("DUONGK.INP", "r")) {
        freopen("DUONGK.INP", "r", stdin);
        freopen("DUONGK.OUT", "w", stdout);
    }
    int n, m, q;
    scanf("%d %d %d", &n, &m, &q);
    vector<int> eu(m), ev(m);
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &eu[i], &ev[i]);
        eu[i]--; ev[i]--;
    }
    while (q--) {
        int s, t; ll K;
        scanf("%d %d %lld", &s, &t, &K);
        vector<ll> cnt(n, 0);            // cnt[v]: số hành trình từ s tới v
        cnt[s - 1] = 1;
        for (ll step = 0; step < K; step++) {
            vector<ll> nxt(n, 0);
            for (int i = 0; i < m; i++)
                nxt[ev[i]] = (nxt[ev[i]] + cnt[eu[i]]) % MOD;
            cnt = nxt;
        }
        printf("%lld\n", cnt[t - 1]);
    }
    return 0;
}
