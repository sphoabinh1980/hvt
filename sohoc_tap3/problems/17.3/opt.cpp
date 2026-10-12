#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
typedef long long ll;
const int B = 10000, W = 4;            // cơ số 10^4

char sa[60005], sb[60005];

// cắt xâu chữ số thành các khối 4 chữ số tính từ cuối; x[0] thấp nhất
vector<ll> split(const char *s, int len) {
    vector<ll> x;
    for (int e = len; e > 0; e -= W) {
        int st = e - W > 0 ? e - W : 0;
        ll v = 0;
        for (int i = st; i < e; i++) v = v * 10 + (s[i] - '0');
        x.push_back(v);
    }
    return x;
}

int main() {
    if (fopen("TICHLON.INP", "r")) {
        freopen("TICHLON.INP", "r", stdin);
        freopen("TICHLON.OUT", "w", stdout);
    }
    scanf("%s %s", sa, sb);
    bool na = sa[0] == '-', nb = sb[0] == '-';
    const char *pa = sa + na, *pb = sb + nb;
    vector<ll> x = split(pa, strlen(pa)), y = split(pb, strlen(pb));
    int n = x.size(), m = y.size();
    vector<ll> c(n + m + 1, 0);
    for (int i = 0; i < n; i++)          // cộng dồn vào cột i + j
        for (int j = 0; j < m; j++)     // c[k] <= 12 500 * 9999^2 ~ 1,25e12
            c[i + j] += x[i] * y[j];
    for (int k = 0; k + 1 < (int)c.size(); k++) {   // dồn nhớ một lượt
        c[k + 1] += c[k] / B;
        c[k] %= B;
    }
    int top = c.size() - 1;
    while (top > 0 && c[top] == 0) top--;
    if (top == 0 && c[0] == 0) { printf("0\n"); return 0; }   // không in -0
    if (na != nb) printf("-");
    printf("%lld", c[top]);
    for (int k = top - 1; k >= 0; k--) printf("%04lld", c[k]);
    printf("\n");
    return 0;
}
