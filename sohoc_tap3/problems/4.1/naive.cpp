#include <cstdio>
#include <vector>
#include <queue>
using namespace std;
const int B = 4000;                     // chỉ xét lượng nước 0..B

int main() {
    if (fopen("DONGNUOC.INP", "r")) {
        freopen("DONGNUOC.INP", "r", stdin);
        freopen("DONGNUOC.OUT", "w", stdout);
    }
    int n, q;
    scanf("%d %d", &n, &q);
    vector<long long> a(n);
    for (auto& x : a) scanf("%lld", &x);
    vector<bool> seen(B + 1, false);    // seen[v]: đong được v lít
    queue<int> Q;
    seen[0] = true; Q.push(0);
    while (!Q.empty()) {                // loang: đổ vào hoặc múc ra một can
        int v = Q.front(); Q.pop();
        for (long long x : a)
            for (long long w : {v + x, v - x})
                if (w >= 0 && w <= B && !seen[w]) {
                    seen[w] = true;
                    Q.push(w);
                }
    }
    int best = 1;
    while (best <= B && !seen[best]) best++;
    printf("%d\n", best);
    while (q--) {
        long long c;
        scanf("%lld", &c);
        puts(c <= B && seen[c] ? "CO" : "KHONG");
    }
    return 0;
}
