#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
    if (fopen("TANGQUA.INP", "r")) {
        freopen("TANGQUA.INP", "r", stdin);
        freopen("TANGQUA.OUT", "w", stdout);
    }
    long long n, m;
    scanf("%lld %lld", &n, &m);
    int a[20], cnt = 0;
    for (int i = 0; i < n; i++) a[i] = i;          // người i nhận quà a[i]
    do {
        int lucky = 0;
        for (int i = 0; i < n; i++) if (a[i] == i) lucky++;
        if (lucky == m) cnt++;
    } while (next_permutation(a, a + n));
    printf("%d\n", cnt);
    return 0;
}
