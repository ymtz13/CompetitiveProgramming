static MOD: u64 = 998244353;

fn main() {
    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();
    let nd: Vec<u64> = inp.split_whitespace().map(|c| c.parse().unwrap()).collect();

    let n = nd[0];
    let d = nd[1];

    let mut ans = 0;

    for k in 1..=d {
        let c00 = 0; // binom(d-2, k)
        let c01 = 0; // binom(d-2, k-1)
        let c11 = 0; // binom(d-2, k-2)
        let c10 = c01;
    }

    println!("{:?}", (n, d));
}
