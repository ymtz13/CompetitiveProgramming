use std::i32;

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    input();
    let a: Vec<usize> = input()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect();

    let mut cnt = vec![i32::MAX; 2001];

    for v in &a {
        if cnt[*v] == i32::MAX {
            cnt[*v] = 0;
        }
        cnt[*v] += 1;
    }

    let mut min_cnt = i32::MAX;
    let mut ans = 0;
    for (a, c) in cnt.iter().enumerate() {
        if *c < min_cnt {
            min_cnt = *c;
            ans = a;
        } else if *c == min_cnt && a < ans {
            ans = a;
        }
    }

    println!("{}", ans);
}
