const MOD: usize = 998244353;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let m = 91000;

    let mut dp2 = vec![0; m];
    let mut dp3 = vec![0; m];
    dp2[0] = 1;
    dp3[0] = 1;

    let mut ans = 1;
    let mut s = 0;

    for _ in 0..n {
        ans *= 3;
        ans %= MOD;

        let a: usize = read_line().parse().unwrap();
        s += a;

        let mut dp2_nxt = vec![0; m];
        let mut dp3_nxt = vec![0; m];

        for i in 0..m - 500 {
            let j = i + a;

            dp2_nxt[i] += dp2[i];
            dp2_nxt[i] %= MOD;
            dp2_nxt[j] += dp2[i];
            dp2_nxt[j] %= MOD;

            dp3_nxt[i] += dp3[i] * 2;
            dp3_nxt[i] %= MOD;
            dp3_nxt[j] += dp3[i];
            dp3_nxt[j] %= MOD;
        }

        dp2 = dp2_nxt;
        dp3 = dp3_nxt;
    }

    let mut t = 0;
    for i in (s + 1) / 2..=s {
        t += dp3[i];
        t %= MOD;
    }

    if s % 2 == 0 {
        t += MOD - dp2[s / 2];
        t %= MOD;
    }

    let ans = (ans + (MOD - t) * 3) % MOD;
    println!("{ans}");
}
