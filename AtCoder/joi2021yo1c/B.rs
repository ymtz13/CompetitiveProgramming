fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    input();
    let s = input();

    let mut ans = 0;
    for (i, c) in s.trim().chars().enumerate() {
        let x = if i % 2 == 0 { 'I' } else { 'O' };
        if c != x {
            ans += 1;
        }
    }

    println!("{}", ans);
}
