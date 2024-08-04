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
    let (n, t, p) = read_uuu();
    let mut ll = read_vec();
    ll.sort();

    let l = ll[n - p];
    let ans = if l > t { 0 } else { t - l };

    println!("{ans}");
}
