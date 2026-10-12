#include <bits/stdc++.h>
using namespace std;

// Đếm số vui vẻ trong [1, N], N <= 10^18
long long memo[20][1500];   // cách điền k chữ số có tổng bình phương t

long long ways(int k, int t) {
    if (t < 0) return 0;
    if (k == 0) return t == 0;
    long long &r = memo[k][t];
    if (r != -1) return r;
    r = 0;
    for (int d = 0; d <= 9; d++) r += ways(k - 1, t - d * d);
    return r;
}

bool happy(int x) {                       // lặp tổng bình phương chữ số
    set<int> seen;
    while (x != 1 && !seen.count(x)) {
        seen.insert(x);
        int s = 0;
        for (; x > 0; x /= 10) s += (x % 10) * (x % 10);
        x = s;
    }
    return x == 1;
}

int main() {
    long long N;
    cin >> N;
    memset(memo, -1, sizeof memo);
    string s = to_string(N);
    int L = s.size();
    vector<long long> cnt(1500, 0);       // cnt[q]: số x <= N có tổng bp q
    int pre = 0;                          // tổng bình phương phần đã bám N
    for (int i = 0; i < L; i++) {
        int c = s[i] - '0';
        for (int d = 0; d < c; d++)
            for (int q = pre + d * d; q < 1500; q++)
                cnt[q] += ways(L - 1 - i, q - pre - d * d);
        pre += c * c;
    }
    cnt[pre]++;                           // chính N
    long long ans = 0;
    for (int q = 1; q < 1500; q++)        // q = 0 ứng với x = 0: bỏ
        if (happy(q)) ans += cnt[q];
    cout << ans << "\n";
    return 0;
}
