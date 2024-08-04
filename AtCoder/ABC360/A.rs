fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let s = read_line();
    if s == "RMS" || s == "SRM" || s == "RSM" {
        println!("Yes");
    } else {
        println!("No");
    }
}
