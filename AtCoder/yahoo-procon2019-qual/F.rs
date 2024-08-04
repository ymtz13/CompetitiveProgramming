const MOD: usize = 998244353;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let s: Vec<_> = read_line().bytes().collect();
    let n = s.len();
    let n2 = n * 2;

    let mut dp = vec![0; n2 + 1];
    dp[0] = 1;

    let mut nr = 0;
    let mut nb = 0;
    for i in 1..=n {
        let c = (s[i - 1] - b'0') as usize;
        nb += c;
        nr += 2 - c;

        let mut dp_nxt = vec![0; n2 + 1];
        dp_nxt[0] = dp[0];
        for j in 1..=n {
            dp_nxt[j] = (dp[j] + dp[j - 1]) % MOD;
        }

        for j in 0..=n {
            if nr + j < i || nb < j {
                dp_nxt[j] = 0;
            }
        }

        dp = dp_nxt;
        // println!("{dp:?}");
    }

    for i in n + 1..=n2 {
        let mut dp_nxt = vec![0; n2 + 1];
        dp_nxt[0] = dp[0];
        for j in 1..=n2 {
            dp_nxt[j] = (dp[j] + dp[j - 1]) % MOD;
        }

        for j in 0..=n2 {
            if nr + j < i || nb < j {
                dp_nxt[j] = 0;
            }
        }

        dp = dp_nxt;
        // println!("{dp:?}");
    }

    println!("{}", dp[nb]);
}
