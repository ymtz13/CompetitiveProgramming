fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let nk = read_vec();
    let n = nk[0];
    let k = nk[1];
    let aa = read_vec();

    let mut ans = 1;
    let mut r = k;
    for &a in &aa {
        if r < a {
            ans += 1;
            r = k;
        }
        r -= a;
    }

    println!("{ans}");
}
