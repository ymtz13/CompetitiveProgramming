fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let aa: Vec<i64> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();

    let mut inc = vec![aa[0]];
    let mut dec = vec![0];

    for i in 1..n {
        let d = aa[i] - aa[i - 1];
        if d > 0 {
            inc.push(inc[i - 1] + d);
            dec.push(dec[i - 1]);
        } else {
            inc.push(inc[i - 1]);
            dec.push(dec[i - 1] + d);
        }
    }

    let mut ss = vec![];
    for i in 0..n {
        ss.push(inc[i] + dec[i]);
    }

    let mut bb = inc.clone();
    bb.extend(dec.clone().into_iter().map(|c| -c));
    bb.sort();

    let c = bb[n];

    let ans: i64 = bb.iter().map(|&b| (b - c).abs()).sum();

    // println!("{inc:?}");
    // println!("{dec:?}");
    // println!("{ss:?}");
    // println!("{bb:?}");
    println!("{ans}");
}
