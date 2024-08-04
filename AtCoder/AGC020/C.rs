fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    read_line();
    let aa = read_vec();

    let m = 60;
    let ll = 2_002_140 / m; // 33369
    let lf = 2_000_040 / m; // 33334
    let mask = (1 << m) - 1;

    let mut dp = vec![0u64; ll];
    dp[0] = 1;

    let mut s = 0;

    for &a in &aa {
        s += a;
        let q0 = a / m;
        let q1 = q0 + 1;
        let r = a % m;
        for i in (0..=lf).rev() {
            let v = dp[i];
            dp[i + q0] |= (v << r) & mask;
            dp[i + q1] |= (v >> (m - r)) & mask;
        }
    }

    for l in 0..ll {
        let v = dp[l];
        for i in 0..m {
            if v & (1 << i) > 0 {
                let a = l * m + i;
                if a * 2 >= s {
                    println!("{a}");
                    return;
                }
            }
        }
    }
}
