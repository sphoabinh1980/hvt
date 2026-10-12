#include <cstdio>
#include <vector>
using namespace std;

long long s(long long n) {                      // tổng ước thực sự, O(n)
    long long t = 0;
    for (long long d = 1; d < n; d++)
        if (n % d == 0) t += d;
    return t;
}

int main() {
    if (fopen("BANBE.INP", "r")) {
        freopen("BANBE.INP", "r", stdin);
        freopen("BANBE.OUT", "w", stdout);
    }
    long long N, k;
    scanf("%lld %lld", &N, &k);
    vector<pair<long long, long long>> res;
    for (long long a = 1; a <= N; a++) {
        long long b = s(a) - k;                 // ứng viên duy nhất cho a
        if (b > a && b <= N && s(b) == a + k) res.push_back({a, b});
    }
    printf("%d\n", (int)res.size());
    for (auto& p : res) printf("%lld %lld\n", p.first, p.second);
    return 0;
}
