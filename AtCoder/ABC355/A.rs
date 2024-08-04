fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let ab = read_vec();
    let a = ab[0];
    let b = ab[1];

    if a != b {
        println!("{}", 6 - a - b);
    } else {
        println!("{}", -1);
    }
}
