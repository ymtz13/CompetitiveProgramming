use std::cmp::{max, min};

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let s = read_line().into_bytes();
    let k: usize = read_line().parse().unwrap();

    let inf = i64::MAX >> 1;

    let m = s.len() + 10;

    let mut dp = vec![vec![-inf; m]; m];
    dp[0][0] = 0;

    for &c in &s {
        let mut dp_nxt = vec![vec![-inf; m]; m];

        for fs in 0..m {
            for fk in 0..m {
                if fk > 0 {
                    dp_nxt[fs][fk - 1] = max(dp_nxt[fs][fk - 1], dp[fs][fk] + 1);
                }
                dp_nxt[0][0] = max(dp_nxt[0][0], dp[fs][fk]);
            }
        }

        if c == b'o' {
            for fs in 0..m {
                for fk in 0..m {
                    dp_nxt[fs + 1][0] = max(dp_nxt[fs + 1][0], dp[fs][fk]);
                }
            }
        }

        if c == b'f' {
            for fs in 1..=s.len() {
                for fk in 0..=k {
                    dp_nxt[fs - 1][k] = max(dp_nxt[fs - 1][k], dp[fs][fk] + 2);
                }
            }
        }

        dp = dp_nxt;
    }

    let mut ans = 0;
    for fs in 0..=s.len() {
        for fk in 0..=k {
            ans = max(ans, dp[fs][fk]);
        }
    }
    ans = s.len() as i64 - ans;

    println!("{ans}");
}
