fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let qhsd = read_vec();
    let n = read_vec()[0];

    let q = qhsd[0];
    let mut h = qhsd[1];
    let mut s = qhsd[2];
    let mut d = qhsd[3];

    if q * 2 < h {
        h = q * 2;
    }
    if h * 2 < s {
        s = h * 2;
    }
    if s * 2 < d {
        d = s * 2;
    }

    let ans = d * (n / 2) + s * (n % 2);

    println!("{ans}");
}
