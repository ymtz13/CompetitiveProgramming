fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    input();
    let alist = input();
    let blist = input();

    let alist: Vec<i32> = alist
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect();
    let blist: Vec<i32> = blist
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect();

    let mut ans = 0;

    for a in &alist {
        for b in &blist {
            if a <= b {
                ans += 1;
            }
        }
    }

    println!("{}", ans);
}
