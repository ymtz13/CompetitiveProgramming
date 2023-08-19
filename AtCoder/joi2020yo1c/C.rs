fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    input();
    let a: Vec<i32> = input()
        .trim()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect();

    let mut ans = 0;
    let mut curr = 0;
    let mut prev = 0;

    for v in &a {
        if *v < prev {
            curr = 0;
        }
        prev = *v;
        curr += 1;
        ans = std::cmp::max(ans, curr);
    }

    println!("{}", ans);
}
