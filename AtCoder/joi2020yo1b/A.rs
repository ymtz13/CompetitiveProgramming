fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    let abc: Vec<usize> = input()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect();

    let min = abc.iter().min().unwrap();
    let sum: usize = abc.iter().sum();

    println!("{}", sum - min);
}
