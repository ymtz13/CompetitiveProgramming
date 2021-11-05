use std::io;

fn main() {
    let mut n = String::new();
    io::stdin().read_line(&mut n).unwrap();

    let mut a = String::new();
    io::stdin().read_line(&mut a).unwrap();
    let a: Vec<&str> = a.trim().split_whitespace().collect();

    let mut p = 1;
    let mut q = 1;
    for v in a {
        let v: i32 = v.parse().unwrap();
        p *= 3;
        q *= if v%2==0 { 2 } else { 1 };
    }
    println!("{}", p-q);
}
