fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn read_int_vec() -> Vec<i64> {
    input()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect()
}

fn main() {
    input();
    let alist = read_int_vec();

    let mut curr = 0;
    let mut ans = 0;
    for &a in &alist {
        if a == 1 {
            curr += 1;
            ans = std::cmp::max(ans, curr);
        }
        if a == 0 {
            curr = 0;
        }
    }

    println!("{}", ans + 1);
}
