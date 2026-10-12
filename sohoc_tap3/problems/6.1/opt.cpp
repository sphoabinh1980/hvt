#include <cstdio>
#include <vector>
using namespace std;

const int N = 10000000;
char comp[N + 1];                    // comp[x] = 1: x là hợp số (hoặc 0, 1)
int cnt[N + 1];                             // cnt[x] = π(x)

int main() {
    if (fopen("DEMNGUYENTO.INP", "r")) {
        freopen("DEMNGUYENTO.INP", "r", stdin);
        freopen("DEMNGUYENTO.OUT", "w", stdout);
    }
    comp[0] = comp[1] = 1;
    for (long long p = 2; p * p <= N; p++)  // sàng Eratosthenes
        if (!comp[p])
            for (long long j = p * p; j <= N; j += p) comp[j] = 1;
    vector<int> pr;                        // pr[k - 1] = số nguyên tố thứ k
    for (int x = 1; x <= N; x++) {
        cnt[x] = cnt[x - 1] + !comp[x];
        if (!comp[x]) pr.push_back(x);
    }
    int q;
    scanf("%d", &q);
    while (q--) {
        int t, x;
        scanf("%d %d", &t, &x);
        printf("%d\n", t == 1 ? cnt[x] : pr[x - 1]);
    }
    return 0;
}
