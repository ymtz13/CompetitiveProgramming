fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("");
    input
}

fn main() {
    input();
    let s = input();
    let s: Vec<char> = s.trim().chars().collect();

    for (i, c) in s[..s.len() - 1].iter().enumerate() {
        if s[i + 1] == 'J' {
            println!("{}", c);
        }
    }
}
