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
    let (n, k, x) = read_uuu();
    let mut aa = read_vec();
    aa.insert(k, x);

    let ans: Vec<_> = aa.iter().map(|c| c.to_string()).collect();

    println!("{}", ans.join(" "));
}
