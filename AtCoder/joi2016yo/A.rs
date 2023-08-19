fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    let a: usize = input().trim().parse().unwrap();
    let b: usize = input().trim().parse().unwrap();
    let c: usize = input().trim().parse().unwrap();
    let d: usize = input().trim().parse().unwrap();
    let e: usize = input().trim().parse().unwrap();
    let f: usize = input().trim().parse().unwrap();

    let mut x = vec![a, b, c, d];
    let mut y = vec![e, f];

    x.sort();
    y.sort();

    let xsum: usize = x.iter().sum();
    let ysum: usize = y.iter().sum();

    let ans: usize = xsum + ysum - x[0] - y[0];
    println!("{}", ans);
}
