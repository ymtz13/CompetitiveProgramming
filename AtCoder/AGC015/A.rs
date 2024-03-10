fn main() {
    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();
    let inp: Vec<usize> = inp
        .trim()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect();
    let n = inp[0];
    let a = inp[1];
    let b = inp[2];

    if n == 1 {
        println!("{}", if a == b { "1" } else { "0" });
    } else if a > b {
        println!("0");
    } else {
        println!("{}", (b - a) * (n - 2) + 1);
    }
}
