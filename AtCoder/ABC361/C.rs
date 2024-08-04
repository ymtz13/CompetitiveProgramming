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
    let (n, k) = read_uu();
    let mut aa = read_vec();
    aa.sort();

    let mut ans = usize::MAX;
    for i in 0..n {
        let j = i + n - k - 1;
        if j >= n {
            break;
        }

        ans = std::cmp::min(ans, aa[j] - aa[i]);
    }

    println!("{ans}");
}
