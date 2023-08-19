fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    let abc = input();
    let mut abc = abc.trim().split_whitespace().map(|c| c.parse().unwrap());
    let a: i32 = abc.next().unwrap();
    let b: i32 = abc.next().unwrap();
    let c: i32 = abc.next().unwrap();

    for ans in 1..1000010 {
        let d = ans * a + (ans / 7) * b;
        if d >= c {
            println!("{}", ans);
            return;
        }
    }
}
