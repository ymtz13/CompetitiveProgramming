use std::io;

fn main() {
    let mut s = String::new();
    io::stdin().read_line(&mut s).unwrap();

    for i in 0..s.len()-1 {
        if &s[i..i+2] == "AC" {
            println!("Yes");
            return
        }
    }
    println!("No");
}
