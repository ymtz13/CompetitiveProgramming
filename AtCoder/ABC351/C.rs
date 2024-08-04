fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let aa: Vec<i64> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();

    let mut stack = std::collections::VecDeque::new();

    for &a in &aa {
        stack.push_back(a);

        loop {
            let m = stack.len();
            if m >= 2 && stack[m - 1] == stack[m - 2] {
                let v = stack.pop_back().unwrap();
                stack.pop_back();
                stack.push_back(v + 1);
            } else {
                break;
            }
        }
    }

    println!("{}", stack.len());
}
