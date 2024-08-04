fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let mut ans = 0;
    for _ in 0..n {
        let s = read_line();
        if &s[..1] == "T" {
            ans += 1;
        }
    }

    println!("{ans}");
}
