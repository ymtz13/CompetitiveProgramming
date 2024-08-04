fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (usize, usize) {
    let v = read_vec();
    (v[0], v[1])
}

fn main() {
    let aa = read_vec();
    let bb = read_vec();

    let mut ans = "Yes";

    for d in 0..3 {
        if aa[d + 3] <= bb[d] || bb[d + 3] <= aa[d] {
            ans = "No";
        }
    }

    println!("{ans}");
}
