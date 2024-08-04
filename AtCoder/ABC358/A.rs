fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let st = read_line();
    let st: Vec<_> = st.split_whitespace().collect();
    let ans = st[0] == "AtCoder" && st[1] == "Land";
    println!("{}", if ans { "Yes" } else { "No" });
}
