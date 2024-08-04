use std::cmp::{max, min};

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let aa = read_vec();
    let bb = read_vec();

    let mut c = 0i64;
    let mut x = 1_000_000_001;
    let mut ans = n as i64;

    for i in (0..n).rev() {
        let a = aa[i];
        let b = bb[i];

        if a <= b {
            let v = max(b - a + 1, c);
            ans = min(ans, v);

            if a < x {
                c += 1;
            }
        } else {
            x = min(x, a - b);
        }
    }
    ans = min(ans, c);

    println!("{ans}");
}
