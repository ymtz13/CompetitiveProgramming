fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_uuu() -> (usize, usize, usize) {
    let v: Vec<_> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    (v[0], v[1], v[2])
}

fn main() {
    let (n, l, r) = read_uuu();
    let mut ans = vec![];
    for i in 0..n {
        if i < l - 1 || r <= i {
            ans.push((i + 1).to_string());
        } else {
            ans.push((r + l - 1 - i).to_string());
        }
    }

    println!("{}", ans.join(" "));
}
