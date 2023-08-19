fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    let s: i64 = input().trim().parse().unwrap();
    let a: i64 = input().trim().parse().unwrap();
    let b: i64 = input().trim().parse().unwrap();
    println!("{}", std::cmp::max(0, (s - a + b - 1) / b) * 100 + 250);
}
