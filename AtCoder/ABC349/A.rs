fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn main() {
    read_line();
    let ans: i64 = -(read_vec().iter().fold(0, |acc, v| acc + v));
    println!("{}", ans);
}