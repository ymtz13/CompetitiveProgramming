fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("");
    input
}

fn main() {
    let xlr = input();
    let xlr: Vec<i64> = xlr
        .split_whitespace()
        .map(|c| c.parse().expect(""))
        .collect();

    let x = xlr[0];
    let l = xlr[1];
    let r = xlr[2];

    let ans = if x < l {
        l
    } else if x > r {
        r
    } else {
        x
    };

    println!("{}", ans);
}
