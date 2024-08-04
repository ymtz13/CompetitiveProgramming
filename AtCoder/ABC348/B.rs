fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let mut pp = vec![];
    for _ in 0..n {
        let xy = read_vec();
        pp.push((xy[0], xy[1]));
    }

    for (x0, y0) in pp.iter() {
        let mut ans = 0;
        let mut max_dsq = -1;
        for (i, (x, y)) in pp.iter().enumerate() {
            let dx = x - x0;
            let dy = y - y0;
            let dsq = dx * dx + dy * dy;
            if dsq > max_dsq {
                ans = i + 1;
                max_dsq = dsq;
            }
        }
        println!("{}", ans);
    }
}
