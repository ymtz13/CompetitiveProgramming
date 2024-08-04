fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let ans: Vec<_> = (1..=n).map(|v| if v % 3 == 0 { b'x' } else { b'o' }).collect();

    println!("{}", String::from_utf8(ans).unwrap());
}
