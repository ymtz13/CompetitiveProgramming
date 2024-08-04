fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_iii() -> (i64, i64, i64) {
    let v: Vec<_> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    (v[0], v[1], v[2])
}

fn main() {
    let (n, a, b) = read_iii();
    println!("{}", std::cmp::max(0, a + b - n));
}
