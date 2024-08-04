fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let n = read_vec()[0] as usize;
    let aa = read_vec();

    let mut bb = aa.clone();
    bb.sort();

    let m = bb[bb.len() - 2];

    for i in 0..n {
        if aa[i] == m {
            println!("{}", i + 1);
        }
    }
}
