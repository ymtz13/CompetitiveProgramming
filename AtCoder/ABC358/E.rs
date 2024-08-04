const MOD: usize = 998244353;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn pow(mut n: usize, mut x: usize) -> usize {
    let mut r = 1;
    while x > 0 {
        if x & 1 > 0 {
            r *= n;
            r %= MOD;
        }
        n *= n;
        n %= MOD;
        x >>= 1;
    }
    r
}

fn inv(n: usize) -> usize {
    pow(n, MOD - 2)
}

fn main() {
    let k = read_vec()[0];
    let cc = read_vec();

    let mut f = vec![1];
    let mut finv = vec![1];
    for i in 1..=1010 {
        f.push(f.last().unwrap() * i % MOD);
        finv.push(inv(*f.last().unwrap()));
    }

    let binom = |n: usize, k: usize| f[n] * finv[n - k] % MOD * finv[k] % MOD;

    let mut dp = vec![0; k + 1];
    dp[0] = 1;

    for &c in &cc {
        let mut dp_nxt = vec![0; k + 1];

        for lf in 0..=k {
            for lt in lf..=k {
                if lt > lf + c {
                    break;
                }
                let v = dp[lf] * binom(lt, lf) % MOD;
                dp_nxt[lt] += v;
                dp_nxt[lt] %= MOD;
            }
        }

        dp = dp_nxt;
    }

    let mut ans = 0;
    for &v in &dp[1..] {
        ans += v;
        ans %= MOD;
    }

    println!("{ans}");
}
