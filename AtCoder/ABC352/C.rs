fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn main() {
    let n: usize = read_line().parse().unwrap();

    let mut max = 0;
    let mut sum = 0;
    for _ in 0..n {
        let ab = read_vec();
        let a = ab[0];
        let b = ab[1];

        max = std::cmp::max(max, b - a);
        sum += a;
    }

    println!("{}", max + sum)
}
