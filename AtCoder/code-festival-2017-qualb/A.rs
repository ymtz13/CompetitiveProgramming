use std::io;

fn main() {
    let mut s = String::new();
    io::stdin().read_line(&mut s).unwrap();
    let s = s.trim();
    println!("{}", &s[0..s.len() - "FESTIVAL".len()]);
}
