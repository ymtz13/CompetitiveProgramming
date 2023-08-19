use std::collections::HashSet;

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn read_int_vec() -> Vec<usize> {
    input()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect()
}

fn main() {
    input();
    let a = read_int_vec();
    let b = read_int_vec();
    let mut s = HashSet::new();
    for v in &b {
        s.insert(*v);
    }

    let mut ans = 0;
    for v in &a {
        if s.contains(v) {
            ans += 1;
        }
    }

    println!("{}", ans);
}
