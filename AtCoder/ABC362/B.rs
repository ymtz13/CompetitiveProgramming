fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uuu() -> (usize, usize, usize) {
    let v = read_vec();
    (v[0], v[1], v[2])
}

fn main() {
    let (r, g, b) = read_uuu();
    let c = read_line();

    let mut ans = 0;
    if c == "Red" {
        ans = std::cmp::min(g, b);
    }
    if c == "Green" {
        ans = std::cmp::min(r, b);
    }
    if c == "Blue" {
        ans = std::cmp::min(r, g);
    }
    println!("{ans}");
}
