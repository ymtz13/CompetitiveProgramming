fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s)
}

const MOD: usize = 998244353;

fn pow(mut x: usize, mut n: usize) -> usize {
    let mut r = 1;
    while n > 0 {
        if n & 1 == 1 {
            r *= x;
            r %= MOD;
        }
        x *= x;
        x %= MOD;

        n >>= 1;
    }
    r
}

fn main() {
    let nm: Vec<usize> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    let n = nm[0];
    let m = nm[1];

    println!("{}", pow(n, m) * pow(m, n - 1) % MOD);
}
