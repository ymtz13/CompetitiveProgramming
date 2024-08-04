use std::cmp::min;

const MOD: usize = 998244353;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let line = read_line();
    let sk: Vec<_> = line.split_whitespace().collect();
    let s: Vec<_> = sk[0].bytes().collect();
    let k: usize = sk[1].parse().unwrap();

    let mut aa = vec![];
    let mut cnt = 0;
    for &c in &s {
        if c == b'0' {
            aa.push(cnt);
            cnt = 0;
        } else {
            cnt += 1;
        }
    }
    aa.push(cnt);
    aa.reverse();

    let k = min(k, aa.iter().sum());

    let mut dp = vec![vec![0; k + 1]; k + 1];
    dp[0][0] = 1;

    for &a in &aa {
        let mut dpnxt = vec![vec![0; k + 1]; k + 1];

        for i in 0..=k {
            let mut tt = vec![0];
            let mut t = 0;
            for j in 0..=(k - i) {
                t = (t + dp[i][j]) % MOD;
                tt.push(t);

                let l = if j > a { j - a } else { 0 };
                dpnxt[i][j] = (MOD + t - tt[l]) % MOD;
            }
        }

        for i in 0..=k {
            let mut s = 0;
            for j in 0..=i {
                dpnxt[j][i - j] += s;
                dpnxt[j][i - j] %= MOD;
                s += dp[j][i - j];
                s %= MOD;
            }
        }

        dp = dpnxt;
    }

    let mut ans = 0;
    for i in 0..=k {
        ans += dp[i][0];
        ans %= MOD;
    }

    println!("{ans}");
}
