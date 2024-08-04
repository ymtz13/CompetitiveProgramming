fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let n = read_vec()[0];
    let aa = read_vec();
    let ww = read_vec();

    let mut ss = vec![0; n + 1];
    let mut mm = vec![0; n + 1];
    for i in 0..n {
        let a = aa[i];
        let w = ww[i];
        ss[a] += w;
        mm[a] = std::cmp::max(mm[a], w);
    }

    let mut ans = 0;
    for a in 1..=n {
        ans += ss[a] - mm[a];
    }

    println!("{ans}");
}
