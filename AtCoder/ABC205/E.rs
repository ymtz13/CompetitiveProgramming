static MOD: usize = 1_000_000_007;

fn read_line() -> String {
    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();
    String::from(inp.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn pow(base: usize, exponent: usize, modulo: usize) -> usize {
    let mut ret = 1;
    let mut val = base;
    let mut exp = exponent;

    while exp > 0 {
        if exp & 1 == 1 {
            ret *= val;
            ret %= modulo;
        }

        exp >>= 1;
        val *= val;
        val %= modulo;
    }

    ret
}

fn solve(n: usize, m: usize, k: usize) -> usize {
    let mut f = vec![1];
    for i in 1..=n + m {
        f.push(f[f.len() - 1] * i % MOD);
    }

    if m + k < n {
        return 0;
    }

    let p = f[n + m];
    let p = p * pow(f[n], MOD - 2, MOD) % MOD;
    let p = p * pow(f[m], MOD - 2, MOD) % MOD;

    if n <= k {
        return p;
    }

    let q = f[n + m];
    let q = q * pow(f[n - (k + 1)], MOD - 2, MOD) % MOD;
    let q = q * pow(f[m + (k + 1)], MOD - 2, MOD) % MOD;

    (p + MOD - q) % MOD
}

fn main() {
    let nmk = read_vec();
    let n = nmk[0];
    let m = nmk[1];
    let k = nmk[2];

    let ans = solve(n, m, k);
    println!("{:?}", ans);
}
