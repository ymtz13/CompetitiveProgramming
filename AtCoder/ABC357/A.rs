fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (usize, usize) {
    let v = read_vec();
    (v[0], v[1])
}

fn main() {
    let (_, mut m) = read_uu();
    let hh = read_vec();
    let mut ans = 0;

    for &h in &hh {
        if h > m {
            break;
        }
        m -= h;
        ans += 1;
    }

    println!("{ans}");
}
