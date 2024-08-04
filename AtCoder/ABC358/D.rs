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
    let (n, _) = read_uu();
    let mut aa = read_vec();
    let mut bb = read_vec();
    aa.sort();
    bb.sort();

    let mut ia = 0;
    let mut ans = 0;
    for &b in &bb {
        while ia < n && aa[ia] < b {
            ia += 1;
        }
        if ia == n {
            println!("-1");
            return;
        }

        ans += aa[ia];
        ia += 1;
    }

    println!("{ans}");
}
