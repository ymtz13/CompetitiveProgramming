fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let n = read_vec()[0] as usize;
    let aa = read_vec();
    let mut ans = 0;

    for i in 0..30 {
        let mut f = 0;
        let mut cnt = vec![1, 0];
        let mut s = 0;

        for &a in &aa {
            if a & (1 << i) > 0 {
                f ^= 1;
            }
            s += cnt[1 - f];
            cnt[f] += 1;
        }

        ans += s * (1 << i);
    }

    let s: i64 = aa.iter().sum();
    ans -= s;

    println!("{ans}");
}
