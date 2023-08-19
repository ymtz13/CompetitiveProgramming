fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    input();
    let s = input();
    let s = s.trim();

    let mut ans = 0;
    let mut prev = '_';

    for c in s.chars() {
        if prev != '_' && prev != c {
            ans += 1;
            prev = '_'
        } else if prev == '_' {
            prev = c;
        }
    }

    println!("{}", ans);
}
