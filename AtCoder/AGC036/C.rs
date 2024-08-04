const MOD: usize = 998244353;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn exp(mut x: usize, mut k: usize) -> usize {
    let mut r = 1;
    while k > 0 {
        if k & 1 == 1 {
            r *= x;
            r %= MOD;
        }
        x *= x;
        x %= MOD;
        k >>= 1;
    }
    r
}

fn inv(x: usize) -> usize {
    exp(x, MOD - 2)
}

fn binom(ff: &Vec<usize>, n: usize, k: usize) -> usize {
    ff[n] * inv(ff[k]) % MOD * inv(ff[n - k]) % MOD
}

fn main() {
    let nm: Vec<_> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    let n = nm[0];
    let m = nm[1];

    let mut ff = vec![1];
    let mut f = 1;
    for i in 1..2_000_000 {
        f *= i;
        f %= MOD;
        ff.push(f);
    }

    let mut ans = 0;

    for k in 0..=n {
        if k > m {
            break;
        }
        if k % 2 != m % 2 {
            continue;
        }

        let a = binom(&ff, n, k);

        let b = (3 * m - k) / 2;

        let c = binom(&ff, b + n - 1, n - 1);
        let mut x = c;

        let d = binom(&ff, b - m + n - 1, n - 1);
        x += MOD - k * d % MOD;
        x %= MOD;

        if b > m {
            let e = binom(&ff, b - (m + 1) + n - 1, n - 1);
            x += MOD - (n - k) * e % MOD;
            x %= MOD;
            // println!("k:{k}, a:{a} b:{b} c:{c} d:{d} e:{e}");
        }

        ans += a * x % MOD;
        ans %= MOD;
    }

    println!("{ans}");
}
