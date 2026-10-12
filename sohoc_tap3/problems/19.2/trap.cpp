#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;

int main() {
    if (fopen("DOANDAI.INP", "r")) {
        freopen("DOANDAI.INP", "r", stdin);
        freopen("DOANDAI.OUT", "w", stdout);
    }
    int n, k;
    scanf("%d %d", &n, &k);
    // first[d]: chỉ số i nhỏ nhất có S_i mod k = d (-1: chưa gặp)
    vector<int> first(k, -1);
    first[0] = 0;                       // S0 = 0
    ll S = 0; int bestLen = 0, bestL = 0;
    for (int r = 1; r <= n; r++) {
        ll x;
        scanf("%lld", &x);
        S += x;
        int s = S % k;                  // BẪY: S < 0 cho s < 0
        if (first[s] == -1) first[s] = r;
        else if (r - first[s] > bestLen) {  // chỉ cập nhật khi dài hơn hẳn
            bestLen = r - first[s];
            bestL = first[s] + 1;
        }
    }
    if (bestLen == 0) printf("0\n");
    else printf("%d %d\n", bestLen, bestL);
    return 0;
}
