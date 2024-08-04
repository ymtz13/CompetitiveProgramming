fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let s = read_line();
    let ss = &s[3..];
    let n: usize = ss.parse().unwrap();

    println!("{}", if 1 <= n && n < 350 && n != 316 { "Yes" } else { "No" });
}
