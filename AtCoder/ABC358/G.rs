fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (usize, usize) {
    let v = read_vec();
    (v[0] as usize, v[1] as usize)
}

fn read_uuu() -> (usize, usize, usize) {
    let v = read_vec();
    (v[0] as usize, v[1] as usize, v[2] as usize)
}

use std::cmp::{max, min};

fn main() {
    let (h, w, k) = read_uuu();
    let (si, sj) = read_uu();

    let mut aaa = vec![];
    for _ in 0..h {
        let aa = read_vec();
        aaa.push(aa);
    }

    let mut dp = vec![vec![i64::MIN; w + 2]; h + 2];
    dp[si][sj] = 0;

    let l = min(k, h * w);

    for _ in 0..l {
        let mut dp_nxt = vec![vec![i64::MIN; w + 2]; h + 2];
        for i in 1..=h {
            for j in 1..=w {
                dp_nxt[i][j] = max(dp_nxt[i][j], dp[i][j]);
                dp_nxt[i][j] = max(dp_nxt[i][j], dp[i - 1][j]);
                dp_nxt[i][j] = max(dp_nxt[i][j], dp[i + 1][j]);
                dp_nxt[i][j] = max(dp_nxt[i][j], dp[i][j - 1]);
                dp_nxt[i][j] = max(dp_nxt[i][j], dp[i][j + 1]);
                if dp_nxt[i][j] >= 0 {
                    dp_nxt[i][j] += aaa[i - 1][j - 1];
                }
            }
        }
        dp = dp_nxt;
    }

    let mut ans = 0;
    for i in 1..=h {
        for j in 1..=w {
            ans = max(ans, dp[i][j] + aaa[i - 1][j - 1] * (k - l) as i64);
        }
    }

    println!("{ans}");
}
