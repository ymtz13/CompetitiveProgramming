fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let np = read_vec();
    let n = np[0];
    let p = np[1];

    let aa = read_vec();

    let n1 = aa.iter().filter(|&a| a % 2 == 1).count();

    let ans: usize;
    if n1 == 0 {
        if p == 0 {
            ans = 1 << n;
        } else {
            ans = 0;
        }
    } else {
        ans = 1 << (n - 1);
    }

    println!("{ans}");
}
