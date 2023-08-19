use std::collections::HashSet;

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("");
    input
}

fn main() {
    input();
    let s = input();
    let s = s.trim();

    let mut set = HashSet::new();
    for c in s.chars() {
        set.insert(c);
    }

    println!("{}", if set.len() >= 3 { "Yes" } else { "No" });
}
