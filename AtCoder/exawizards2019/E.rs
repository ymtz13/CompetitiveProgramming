const MOD: usize = 1_000_000_007;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_uu() -> (usize, usize) {
    let a: Vec<_> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    (a[0], a[1])
}

fn pow(mut n: usize, mut p: usize) -> usize {
    let mut r = 1;
    while p > 0 {
        if p & 1 == 1 {
            r *= n;
            r %= MOD;
        }
        n *= n;
        n %= MOD;
        p >>= 1;
    }
    r
}

fn inv(n: usize) -> usize {
    pow(n, MOD - 2)
}

fn main() {
    let mut f = 1;
    let mut ff = vec![1];
    for i in 1..200010 {
        f = f * i % MOD;
        ff.push(f);
    }

    let binom = |n: usize, k: usize| (ff[n] * inv(ff[n - k]) % MOD) * inv(ff[k]) % MOD;

    let (b, w) = read_uu();

    let mut cw = 0;
    let mut cb = 0;

    for i in 0..(b + w) {
        let all = pow(2, i);

        if w <= i {
            cw *= 2;
            cw += binom(i - 1, w - 1);
            cw %= MOD;
        }

        if b <= i {
            cb *= 2;
            cb += binom(i - 1, b - 1);
            cb %= MOD;
        }

        let rem = all + MOD - cw + MOD - cb;
        let nb = cw * 2 + rem;
        let denom = all * 2;

        let ans = nb * inv(denom) % MOD;
        let ans = (ans + MOD) % MOD;

        println!("{ans}")
    }
}
