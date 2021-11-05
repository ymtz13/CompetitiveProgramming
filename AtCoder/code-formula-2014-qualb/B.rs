use std::io;

fn main() {
    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("");

    let (mut so, mut se) = (0, 0);

    for (i, c) in n.trim().chars().rev().enumerate() {
        let d = match c.to_digit(10) {
            Some(v) => v,
            None => 0,
        };

        match i % 2 {
            0 => { so += d; },
            _ => { se += d; },
        };
    }

    println!("{} {}", se, so);
}
