const MOD: usize = 1_000_000_007;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    read_line();
    let aa = read_vec();

    let offset = 1020;
    let m = offset * 2;
    let mut dp = vec![0usize; m];
    dp[0 + offset] = 1;

    let mut cc0 = vec![1];

    for i in 0..aa.len() {
        let a = aa[i];
        let mut dp_nxt = dp.clone();
        for f in -1000..=1000 {
            if f == 0 {
                continue;
            }
            dp_nxt[(offset as i64 + f + a) as usize] += dp[(offset as i64 + f) as usize];
            dp_nxt[(offset as i64 + f + a) as usize] %= MOD;
        }

        let mut exists = vec![false; 21];
        for j in (0..i).rev() {
            exists[(aa[j] + 10) as usize] = true;
            let c = cc0[j];

            for k in -10..=10 {
                if k == 0 || !exists[(k + 10) as usize] {
                    continue;
                }
                dp_nxt[(offset as i64 + a + k) as usize] += c;
                dp_nxt[(offset as i64 + a + k) as usize] %= MOD;
            }
        }

        let c0 = dp_nxt[0 + offset] + MOD - dp[0 + offset];
        cc0.push(c0);

        dp = dp_nxt;
    }

    let mut ans = 0;
    for &v in &dp {
        ans += v;
        ans %= MOD;
    }
    println!("{ans}");
}
