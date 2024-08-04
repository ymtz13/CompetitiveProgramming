fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn main() {
    let nq = read_vec();
    let n = nq[0];
    let q = nq[1];
    let tt = read_vec();

    let mut ans = vec![1; n];
    for &t in &tt {
        ans[t - 1] = 1 - ans[t - 1];
    }

    println!("{}", ans.iter().fold(0, |acc, v| acc + v));
}
