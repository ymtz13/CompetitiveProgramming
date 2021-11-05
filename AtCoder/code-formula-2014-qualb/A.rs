use std::io;

fn main() {
    let mut a = String::new();
    io::stdin().read_line(&mut a).expect("");
    let a: u8 = a.trim().parse().expect("");

    println!("{}", 7 - a);
}
