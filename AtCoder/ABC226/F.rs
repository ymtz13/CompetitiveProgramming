const MOD: usize = 998244353;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn gcd(mut a: usize, mut b: usize) -> usize {
    while b > 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn lcm(a: usize, b: usize) -> usize {
    a * b / gcd(a, b)
}

fn pow(mut n: usize, mut x: usize) -> usize {
    let mut r = 1;
    while x > 0 {
        if x & 1 == 1 {
            r *= n;
            r %= MOD;
        }

        n *= n;
        n %= MOD;
        x >>= 1;
    }
    r
}

fn main() {
    let nk = read_vec();
    let n = nk[0];
    let k = nk[1];

    let smax = 200_000;
    let mut dp = vec![vec![0; smax]; n + 1];
    dp[0][1] = 1;

    for i in 1..=n {
        let mut f = 1;
        for m in 1..=i {
            for s in 1..smax {
                if dp[i - m][s] == 0 {
                    continue;
                }

                let l = lcm(s, m);
                dp[i][l] += dp[i - m][s] * f % MOD;
                dp[i][l] %= MOD;
            }

            f *= i - m;
            f %= MOD;
        }
    }

    let mut ans = 0;
    for s in 1..smax {
        let c = dp[n][s];
        if c == 0 {
            continue;
        }
        let s_k = pow(s, k);
        ans += s_k * c % MOD;
        ans %= MOD;
    }

    println!("{ans}");
}
