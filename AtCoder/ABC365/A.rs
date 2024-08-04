fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let y = read_vec()[0];

    let ans = if y % 4 > 0 {
        365
    } else if y % 100 > 0 {
        366
    } else if y % 400 > 0 {
        365
    } else {
        366
    };

    println!("{ans}");
}
