fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("");
    input
}

fn read_int_vec() -> Vec<usize> {
    input()
        .split_whitespace()
        .map(|c| c.parse().expect(""))
        .collect()
}

fn main() {
    let n: usize = input().trim().parse().expect("");
    let a = read_int_vec();

    let mut ans = n * (n + 1);
    for v in a {
        ans -= v;
    }

    println!("{}", ans);
}
