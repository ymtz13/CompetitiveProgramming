fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("");
    input
}

fn main() {
    input();
    let s = input();
    let s = s.trim();

    let n = s.len();

    let s1 = &s[..n / 2];
    let s2 = &s[n / 2..];

    println!("{}", if s1 == s2 { "Yes" } else { "No" });
}
