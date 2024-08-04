fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let mut vv = vec![];

    let mut ans = 0;

    for _ in 0..n {
        let s = read_line().into_bytes();

        let mut cx = 0;
        let mut d = 0;
        for &c in &s {
            if c == b'X' {
                cx += 1;
            } else {
                let x = (c - b'0') as i64;
                d += x;
                ans += cx * x;
            }
        }

        vv.push((cx, d));
    }

    vv.sort_by(|&(cx1, d1), &(cx2, d2)| (cx1 * d2).partial_cmp(&(cx2 * d1)).unwrap());

    let mut dd = 0;
    for &(cx, d) in &vv {
        ans += cx * dd;
        dd += d;
    }

    println!("{ans}");
}
