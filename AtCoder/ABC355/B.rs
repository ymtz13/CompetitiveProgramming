fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let nm = read_vec();
    let aa = read_vec();
    let bb = read_vec();

    let mut cc = aa.clone();
    cc.extend(bb);
    cc.sort();

    for i in 1..cc.len() {
        let v1 = cc[i];
        let v0 = cc[i - 1];
        if aa.contains(&v0) && aa.contains(&v1) {
            println!("Yes");
            return;
        }
    }

    println!("No");
}
