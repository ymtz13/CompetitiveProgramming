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
    let mut ss = read_line();
    let mut s: Vec<_> = ss.clone().bytes().collect();

    let mut n = 0;
    for &c in &s {
        if c < b'a' {
            n += 1;
        }
    }

    if n * 2 > s.len() {
        ss.make_ascii_uppercase();
    } else {
        ss.make_ascii_lowercase();
    }

    println!("{ss}");
}
