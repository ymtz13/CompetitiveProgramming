use std::cmp::{max, min};

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let r: usize = read_line().parse().unwrap();
    let r = r % 100;
    let ans = 100 - r;

    println!("{ans}");
}
