fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("");
    input
}

fn main() {
    input();
    let s = input();
    let s = s.trim();

    let mut current = 1;
    let mut ans = 0;

    for c in s.chars() {
        if c == 'L' {
            current = std::cmp::max(1, current - 1);
        } else {
            current = std::cmp::min(3, current + 1);
        }
        if current == 3 {
            ans += 1
        }
    }

    println!("{}", ans);
}
