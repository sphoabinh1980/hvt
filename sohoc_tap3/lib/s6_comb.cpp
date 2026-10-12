// C(n, k) mod p nguyên tố, p > N: chuẩn bị O(N + log p), mỗi truy vấn O(1)
const ll P = 1000000007;
vector<ll> fact, ifact;
void initComb(int N) {
    fact.assign(N + 1, 1); ifact.assign(N + 1, 1);
    for (int i = 1; i <= N; i++) fact[i] = fact[i - 1] * i % P;
    ifact[N] = power(fact[N], P - 2, P);  // định lí Fermat nhỏ
    for (int i = N; i > 0; i--) ifact[i - 1] = ifact[i] * i % P;
}
ll C(int n, int k) {
    if (k < 0 || k > n) return 0;
    return fact[n] * ifact[k] % P * ifact[n - k] % P;
}
