fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let s = read_line();
    let n: usize = read_line().parse().unwrap();
    let tt: Vec<_> = (0..n).map(|_| read_line().into_bytes()).collect();

    let mut ans = vec![];
    for c in s.split_whitespace() {
        let c = c.to_string();
        let cb = c.clone().into_bytes();
        let mut ng = false;

        for t in &tt {
            if c.len() != t.len() {
                continue;
            }

            if cb.iter().zip(t.iter()).all(|(cc, tt)| tt == cc || *tt == b'*') {
                ng = true;
                break;
            }
        }

        ans.push(if ng { "*".repeat(c.len()) } else { c.to_string() })
    }

    println!("{}", ans.join(" "));
}
