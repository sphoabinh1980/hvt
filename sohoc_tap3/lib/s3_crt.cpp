// ghép x ≡ r1 (mod m1) và x ≡ r2 (mod m2) thành x ≡ r (mod lcm)
// trả về false nếu vô nghiệm; giả sử lcm(m1, m2) vừa long long
bool crt(ll r1, ll m1, ll r2, ll m2, ll &r, ll &m) {
    ll p, q, g = extgcd(m1, m2, p, q);    // m1 p + m2 q = g
    if ((r2 - r1) % g != 0) return false;
    ll l = m1 / g * m2;
    ll t = mulmod(md((r2 - r1) / g, m2 / g), md(p, m2 / g), m2 / g);
    r = md(r1 + mulmod(t, m1, l), l);     // x = r1 + m1 * t
    m = l;
    return true;
}
