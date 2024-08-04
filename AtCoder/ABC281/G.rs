fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn pow(mut n: usize, mut x: usize, m: usize) -> usize {
    let mut r = 1;
    while x > 0 {
        if x & 1 == 1 {
            r *= n;
            r %= m;
        }

        n *= n;
        n %= m;
        x >>= 1;
    }
    r
}

fn main() {
    let nm = read_vec();
    let n = nm[0];
    let m = nm[1];

    let mut binom = vec![vec![0; n + 1]; n + 1];
    for i in 0..=n {
        binom[i][0] = 1;
        for j in 1..=i {
            binom[i][j] = (binom[i - 1][j] + binom[i - 1][j - 1]) % m;
        }
    }

    let mut dp = vec![vec![0; n - 1]; n];
    dp[1][1] = 1;

    for i in 2..n {
        for p in 1..i {
            let j = i - p;
            let mut v = 0;
            for q in 1..=j {
                let w = dp[j][q];
                let x = pow(pow(2, q, m) + m - 1, p, m);
                let b = binom[n - 1 - j][p];
                let c = pow(2, p * (p - 1) / 2, m);
                v += w * x % m * b % m * c % m;
                v %= m;
            }
            dp[i][p] = v;
        }
    }

    let mut ans = 0;
    for q in 1..n - 1 {
        let w = dp[n - 1][q];
        let x = pow(2, q, m) + m - 1;
        ans += w * x % m;
        ans %= m;
    }

    println!("{ans}");
}
