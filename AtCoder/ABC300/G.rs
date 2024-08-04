fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let np: Vec<usize> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    let n = np[0];
    let p = np[1];

    let primes = vec![
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 87, 89, 97,
    ];

    println!("{:?}", ((primes[0] as f64).log2(), primes.len()));

    let x = 10_000_000_000_000_000.0f64;
    let logx = x.log10();
    let logw = (x - 1.).log10();
    println!("{:?}", (logx, logw, logx - logw));
}
