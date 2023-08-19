use std::io;

fn input() -> String {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("");
    input
}

fn read_int_vec() -> Vec<i64> {
    input()
        .split_whitespace()
        .map(|c| c.parse().expect(""))
        .collect()
}

fn main() {
    input();
    let mut a = read_int_vec();
    let mut b = read_int_vec();

    a.append(&mut b);
    a.sort();

    for v in a {
        println!("{}", v);
    }
}
