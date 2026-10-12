// lũy thừa ma trận vuông theo mô-đun P (phần tử < P ~ 10^9)
typedef vector<vector<ll>> Mat;
Mat mul(const Mat &a, const Mat &b) {
    int n = a.size();
    Mat c(n, vector<ll>(n, 0));
    for (int i = 0; i < n; i++)
        for (int t = 0; t < n; t++)
            for (int j = 0; j < n; j++)   // lấy dư sau mỗi phép cộng
                c[i][j] = (c[i][j] + a[i][t] * b[t][j]) % P;
    return c;
}
Mat matPow(Mat b, ll e) {
    int n = b.size();
    Mat r(n, vector<ll>(n, 0));
    for (int i = 0; i < n; i++) r[i][i] = 1 % P;   // ma trận đơn vị
    for (; e > 0; e >>= 1, b = mul(b, b))
        if (e & 1) r = mul(r, b);
    return r;
}
