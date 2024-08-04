const MOD: usize = 998244353;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_uu() -> (usize, usize) {
    let v: Vec<_> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    (v[0], v[1])
}

fn main() {
    let (mut n, m) = read_uu();
    n += 1;

    let mut ans = 0;
    let mut s = 0;
    for i in 0..62 {
        let k = 1 << i;

        if m & k > 0 {
            if n & 1 == 1 {
                ans += s;
            }

            ans += (n / 2) % MOD * (k % MOD);
            ans %= MOD;
        }

        s += (n & 1) * k;
        s %= MOD;
        n >>= 1;
    }

    println!("{ans}");
}
