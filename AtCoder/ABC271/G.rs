const MOD: usize = 998244353;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uuu() -> (usize, usize, usize) {
    let v = read_vec();
    (v[0], v[1], v[2])
}

fn main() {
    let (n, x, y) = read_uuu();
    let cc = read_line();
    let cc: Vec<_> = cc.bytes().map(|v| v == b'A').collect();

    println!("{cc:?}");
}
