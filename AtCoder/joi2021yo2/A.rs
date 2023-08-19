use std::collections::VecDeque;

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    let na = input();
    let mut na = na.split_whitespace().map(|c| c.parse().unwrap());
    let n = na.next().unwrap();
    let mut a = na.next().unwrap();

    let s = input();
    let s = s.trim();

    let mut xl = VecDeque::new();
    let mut xr = VecDeque::new();

    for (i, c) in s.chars().enumerate() {
        let i = i + 1;
        if c == '#' {
            if i < a {
                xl.push_front(i);
            } else {
                xr.push_back(i);
            }
        }
    }

    let mut ans = 0;

    loop {
        if xl.is_empty() && xr.is_empty() {
            break;
        }

        let x = match xr.pop_front() {
            Some(v) => v,
            None => n + 1,
        };
        ans += x - a;
        a = x;

        if xl.is_empty() && xr.is_empty() {
            break;
        }

        let x = match xl.pop_front() {
            Some(v) => v,
            None => 0,
        };
        ans += a - x;
        a = x;
    }

    println!("{}", ans);
}
