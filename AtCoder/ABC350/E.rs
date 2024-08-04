use std::collections::HashMap;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_uuuu() -> (usize, usize, usize, usize) {
    let vv: Vec<_> = read_line().split_whitespace().map(|v| v.parse().unwrap()).collect();
    (vv[0], vv[1], vv[2], vv[3])
}

fn dfs(memo: &mut HashMap<usize, f64>, n: usize, a: usize, x: f64, y: f64) -> f64 {
    if n == 0 {
        return 0.0;
    }
    if memo.contains_key(&n) {
        return *memo.get(&n).unwrap();
    }

    let ra = dfs(memo, n / a, a, x, y) + x;

    let mut rb = 0.0;
    for b in 2..=6 {
        rb += dfs(memo, n / b, a, x, y);
    }
    rb /= 5.0;
    rb += y * 1.2;

    let r = if ra < rb { ra } else { rb };

    memo.insert(n, r);

    r
}

fn main() {
    let (n, a, x, y) = read_uuuu();

    let mut memo = HashMap::new();
    let ans = dfs(&mut memo, n, a, x as f64, y as f64);

    println!("{ans}");
}
