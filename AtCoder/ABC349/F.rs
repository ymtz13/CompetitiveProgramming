fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn f(x: usize) -> Vec<(usize, usize)> {}

fn main() {
    let nm = read_vec();
    let n = nm[0];
    let m = nm[1];

    let aa = read_vec();
}
