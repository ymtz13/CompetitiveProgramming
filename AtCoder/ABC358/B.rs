fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_ii() -> (i64, i64) {
    let v = read_vec();
    (v[0], v[1])
}

fn main() {
    let (_, a) = read_ii();
    let tt = read_vec();

    let mut ans = vec![];
    let mut nxt = a;

    for &t in &tt {
        let b = std::cmp::max(t + a, nxt);
        nxt = b + a;
        ans.push(b);
    }

    for &a in &ans {
        println!("{a}");
    }
}
