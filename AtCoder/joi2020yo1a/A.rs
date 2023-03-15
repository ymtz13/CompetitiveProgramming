use std::io;

fn parseInt(&str)

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("");

    let v: Vec<&str> = input.split(' ').collect();

    let a: i64 = v[0].trim().parse().expect("");
    let b: i64 = v[1].trim().parse().expect("");
    let c: i64 = v[2].trim().parse().expect("");

    if a + b + c <= 4 {
        println!("1");
    } else {
        println!("2");
    }

    // println!("hello, {:#?}, {}, {}, {}", v, a, b, c);
}
