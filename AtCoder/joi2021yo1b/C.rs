use std::io;

fn input() -> String {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("");
    input
}

fn main() {
    input();
    let input = input();
    let a: Vec<i32> = input
        .split_whitespace()
        .map(|s| s.parse().expect(""))
        .collect();

    let max = *(a.iter().max().unwrap());

    let mut ans = (0, 0);
    let mut visited_max = false;

    for v in a {
        if v == max {
            visited_max = true;
        } else if visited_max {
            ans.1 += v;
        } else {
            ans.0 += v;
        }
    }

    println!("{}", ans.0);
    println!("{}", ans.1);
}
