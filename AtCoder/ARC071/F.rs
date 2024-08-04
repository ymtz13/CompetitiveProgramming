const MOD: usize = 1_000_000_007;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let n: usize = read_line().parse().unwrap();

    if n == 1 {
        println!("1");
        return;
    }

    let mut s = 2;
    let mut dp = vec![1, 1];

    for l in 2..n {
        let v = (s + MOD - dp[l - 2]) % MOD;
        s += v;
        s %= MOD;
        dp.push(v);
    }

    let mut ans = 0;
    for l in 0..n - 2 {
        let c = (l + 2 + (n - 1) * (n - 1)) % MOD;
        let a = dp[l] * c % MOD;
        ans += a;
        ans %= MOD;
    }

    ans += dp[n - 2] * (n - 1) % MOD * n % MOD;
    ans %= MOD;

    ans += dp[n - 1] * n % MOD;
    ans %= MOD;

    println!("{ans}");
}
