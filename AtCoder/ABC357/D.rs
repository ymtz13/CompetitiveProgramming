const MOD: u128 = 998244353;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<u128> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (u128, u128) {
    let v = read_vec();
    (v[0], v[1])
}

fn pow(mut n: u128, mut x: u128) -> u128 {
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
    let n = read_line();
    let d = n.len() as u128;
    let n: u128 = n.parse().unwrap();

    let pow10 = pow(10, d);

    let mut x = 1;
    let mut z = 0;
    let mut l = pow10;

    for i in 0..61 {
        let k = 1 << i;
        if n & k > 0 {
            z *= pow(pow(10, k), d);
            z %= MOD;

            z += x;
            z %= MOD;
        }

        x += x * l;
        x %= MOD;

        l *= l;
        l %= MOD;
    }

    let ans = z * n % MOD;
    println!("{ans}");
}
