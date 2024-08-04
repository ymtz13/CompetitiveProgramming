fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let mut s = read_line().into_bytes();
    let t: Vec<_> = read_line().into_bytes().iter().map(|c| c + 32).collect();

    s.push(b'x');

    let mut it = 0;
    for &c in &s {
        if c == t[it] {
            it += 1;
        }
        if it == 3 {
            break;
        }
    }

    println!("{}", if it == 3 { "Yes" } else { "No" });
}
