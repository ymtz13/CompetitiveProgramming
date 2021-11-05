use std::io;

fn main() {
    let mut s = String::new();
    io::stdin().read_line(&mut s).unwrap();

    let xy: Vec<&str> = s.split_whitespace().collect();
    let x1: i64 = if let Ok(v) = xy[0].parse() { v } else { panic!(); };
    let y1: i64 = if let Ok(v) = xy[1].parse() { v } else { panic!(); };

    let mut s = String::new();
    io::stdin().read_line(&mut s).unwrap();

    let xy: Vec<&str> = s.split_whitespace().collect();
    let x2: i64 = if let Ok(v) = xy[0].parse() { v } else { panic!(); };
    let y2: i64 = if let Ok(v) = xy[1].parse() { v } else { panic!(); };

    println!("{}", (x2-x1).abs() + (y2-y1).abs() + 1);
}
