fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let s = read_line().into_bytes();

    let mut ans: usize = 0;
    let mut cnt: usize = 0;
    for i in 0..s.len() {
        if s[i] == b'W' {
            ans += i - cnt;
            cnt += 1;
        }
    }

    println!("{ans}");
}
