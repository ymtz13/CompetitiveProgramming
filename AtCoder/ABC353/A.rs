fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let hh = read_vec();

    let h0 = hh[0];
    for i in 2..=n {
        if hh[i - 1] > h0 {
            println!("{i}");
            return;
        }
    }

    println!("-1");
}
