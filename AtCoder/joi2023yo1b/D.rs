fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("");
    input
}

fn read_int_vec() -> Vec<usize> {
    input()
        .split_whitespace()
        .map(|c| c.parse().expect(""))
        .collect()
}

fn main() {
    input();
    let a = read_int_vec();
    input();
    let b = read_int_vec();

    let mut s = std::collections::HashSet::new();
    for v in b {
        s.insert(v);
    }

    let mut ans = 0;

    for v in a.iter() {
        ans += v;

        if s.contains(&ans) {
            ans = 0;
        }
    }

    println!("{}", ans);
}
