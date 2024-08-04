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

fn inv(x: usize) -> usize {
    pow(x, MOD - 2)
}

fn main() {
    let nk = read_vec();
    let n = nk[0] as usize;
    let k = nk[1];

    let ninv = inv(n);
    let ninv2 = ninv * ninv % MOD;

    let u11 = (1 + (n - 1) * (n - 1) % MOD) * ninv2 % MOD;
    let ux1 = ninv2 * 2 % MOD;

    let mut p1 = 1;

    for _ in 0..k {
        p1 = p1 * u11 % MOD + (1 + MOD - p1) * ux1 % MOD;
        p1 %= MOD;
    }

    let ans = p1 + (2 + n) * inv(2) % MOD * (1 + MOD - p1) % MOD;
    let ans = ans % MOD;

    println!("{ans}");
}
