fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let v: Vec<f64> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    let n = v[0];
    let s = v[1];
    let t = v[2];
    let a = v[3];
    let b = v[4];

    let f = |e: f64| {
        let q = (e / a).floor();

        let m = if q < t { q } else { t };
        let v = (m * (m + 1.0) / 2.0) * a;

        let m1 = if m < t { m + 1.0 } else { t };
        let z = m1 * (e - m * a);

        v + z
    };

    // println!("10 {}", f(10.0));
    // println!("11 {}", f(11.0));
    // println!("12 {}", f(12.0));
    // println!("20 {}", f(20.0));
    // println!("21 {}", f(21.0));
    // println!("30 {}", f(30.0));
    // println!("31 {}", f(31.0));
    // println!("40 {}", f(40.0));
    // println!("41 {}", f(41.0));
    // println!("50 {}", f(50.0));
    // println!("51 {}", f(51.0));
    // return;

    let mut ok = 0.0;
    let mut ng = 1e20;
    while ng - ok > 1e-8 && 1.0 - (ok / ng) > 1e-8 {
        let tgt = (ok + ng) / 2.0;

        let f = f(tgt + b);
        let d = n * b - f;

        if d > 0.0 {
            ok = tgt;
        } else {
            ng = tgt;
        }
        // println!("{ok} {ng}");
    }

    let mut ans = ok + b;

    if s <= t && (t - s) * a < ans {
        ans = (t - s) * a;
    }

    println!("{ans}");
}
