use std::cmp::max;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let s = read_line().into_bytes();
    let k: usize = read_line().parse().unwrap();

    println!("{s:?}");

    let inf = i64::MAX >> 1;

    let mut dp = vec![vec![-inf; k + 1]; s.len() + 1];
    dp[0][0] = 0;

    for &c in &s {
        let mut dp_nxt = vec![vec![-inf; k + 1]; s.len() + 1];

        if c == b'o' {
            for fs in 0..=s.len() {
                for fk in 0..=k {
                    if fk > 0 {
                        dp_nxt[fs][fk - 1] = max(dp_nxt[fs][fk - 1], dp[fs][fk] + 1);
                    }
                    if fs < s.len() {
                        dp_nxt[fs + 1][0] = max(dp_nxt[fs + 1][0], dp[fs][fk]);
                    }
                }
            }
        } else if c == b'f' {
            for fs in 0..=s.len() {
                for fk in 0..=k {
                    if fk > 0 {
                        dp_nxt[fs][fk - 1] = max(dp_nxt[fs][fk - 1], dp[fs][fk] + 1);
                    }
                    if fs > 0 {
                        dp_nxt[fs - 1][k] = max(dp_nxt[fs - 1][k], dp[fs][fk] + 2);
                    }
                    dp_nxt[0][0] = max(dp_nxt[0][0], dp[fs][fk]);
                }
            }
        } else {
            for fs in 0..=s.len() {
                for fk in 0..=k {
                    if fk > 0 {
                        dp_nxt[fs][fk - 1] = max(dp_nxt[fs][fk - 1], dp[fs][fk] + 1);
                    }
                    dp_nxt[0][0] = max(dp_nxt[0][0], dp[fs][fk]);
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
