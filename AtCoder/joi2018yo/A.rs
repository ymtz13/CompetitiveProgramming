fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn read_int_vec() -> Vec<i64> {
    input()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect()
}

fn main() {
    let input = read_int_vec();
    let n = input[0];
    let a = input[1];
    let b = input[2];
    let c = input[3];
    let d = input[4];

    let vx = (n + a - 1) / a * b;
    let vy = (n + c - 1) / c * d;

    println!("{}", std::cmp::min(vx, vy));
}
