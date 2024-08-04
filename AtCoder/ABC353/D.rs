const MOD: usize = 998244353;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let aa = read_vec();

    let mut ans = 0;

    let mut d = 0;
    for i in (0..n).rev() {
        let a = aa[i];

        ans += a * i;
        ans %= MOD;

        ans += a * d;
        ans %= MOD;

        let l = a.to_string().len();
        d += 10usize.pow(l as u32);
        d %= MOD;
    }

    println!("{ans}");
}
