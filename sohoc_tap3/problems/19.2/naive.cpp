#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("DOANDAI.INP", "r")) {
        freopen("DOANDAI.INP", "r", stdin);
        freopen("DOANDAI.OUT", "w", stdout);
    }
    int n; ll k;
    scanf("%d %lld", &n, &k);
    vector<ll> a(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &a[i]);
    int bestLen = 0, bestL = 0;
    for (int l = 1; l <= n; l++) {
        ll s = 0;
        for (int r = l; r <= n; r++) {
            s += a[r];
            // l tăng dần và chỉ cập nhật khi dài hơn hẳn: giữ l nhỏ nhất
            if (s % k == 0 && r - l + 1 > bestLen) {
                bestLen = r - l + 1;
                bestL = l;
            }
        }
    }
    if (bestLen == 0) printf("0\n");
    else printf("%d %d\n", bestLen, bestL);
    return 0;
}
