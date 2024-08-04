fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let n = read_vec()[0] as usize;
    let ss = read_line().into_bytes();

    let mut dp = vec![0, 0, 0];

    let (r, p, s) = (0, 1, 2);

    for &c in &ss {
        let mut dp_nxt = vec![0, 0, 0];

        if c == b'R' {
            dp_nxt[r] = std::cmp::max(dp[p], dp[s]);
            dp_nxt[p] = std::cmp::max(dp[s], dp[r]) + 1;
        }
        if c == b'P' {
            dp_nxt[p] = std::cmp::max(dp[s], dp[r]);
            dp_nxt[s] = std::cmp::max(dp[r], dp[p]) + 1;
        }
        if c == b'S' {
            dp_nxt[s] = std::cmp::max(dp[r], dp[p]);
            dp_nxt[r] = std::cmp::max(dp[p], dp[s]) + 1;
        }

        dp = dp_nxt;
    }

    println!("{}", dp.iter().max().unwrap());
}
