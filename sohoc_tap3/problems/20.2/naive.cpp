#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long ll;

int n; ll X[100005], Y[100005];

bool onSeg(ll px, ll py, int i) {        // P nằm trên cạnh i -> i+1 ?
    int j = (i + 1) % n;
    ll cr = (X[j] - X[i]) * (py - Y[i]) - (Y[j] - Y[i]) * (px - X[i]);
    return cr == 0 && min(X[i], X[j]) <= px && px <= max(X[i], X[j])
                   && min(Y[i], Y[j]) <= py && py <= max(Y[i], Y[j]);
}

bool inside(ll px, ll py) {              // tia sang phải, đếm số lần cắt
    bool c = false;
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        if ((Y[i] > py) != (Y[j] > py)) {
   // giao điểm có hoành độ X[i] + (py - Y[i]) (X[j] - X[i]) / (Y[j] - Y[i])
            ll num = (py - Y[i]) * (X[j] - X[i]), den = Y[j] - Y[i];
            if (den < 0) { num = -num; den = -den; }
            if ((px - X[i]) * den < num) c = !c;
        }
    }
    return c;
}

int main() {
    if (fopen("DAGIAC.INP", "r")) {
        freopen("DAGIAC.INP", "r", stdin);
        freopen("DAGIAC.OUT", "w", stdout);
    }
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%lld %lld", &X[i], &Y[i]);
    ll x0 = *min_element(X, X + n), x1 = *max_element(X, X + n);
    ll y0 = *min_element(Y, Y + n), y1 = *max_element(Y, Y + n);
    ll I = 0, B = 0;
    for (ll x = x0; x <= x1; x++)
        for (ll y = y0; y <= y1; y++) {
            bool b = false;
            for (int i = 0; i < n && !b; i++) b = onSeg(x, y, i);
            if (b) B++;
            else if (inside(x, y)) I++;
        }
    printf("%lld %lld\n", I, B);
    return 0;
}
