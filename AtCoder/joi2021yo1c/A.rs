fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    let iter = input();
    let mut iter = iter.split_whitespace().map(|c| c.parse::<i32>().unwrap());

    let a = iter.next().unwrap();
    let b = iter.next().unwrap();

    let mut v = vec![a + b, a - b];
    v.sort();
    v.reverse();

    for ans in &v {
        println!("{}", ans);
    }
}
