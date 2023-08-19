fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    input();
    let mut k: usize = input().trim().parse().unwrap();
    let s = input();

    for c in s.chars() {
        if c == 'R' {
            k -= 1;
        }
    }

    println!("{}", if k == 0 { 'W' } else { 'R' });
}
