fn main() {
    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();

    let inp = inp.trim();
    let n = inp.len();

    let mut ans = 0;

    for (i, c) in inp.chars().enumerate() {
        if c == 'U' {
            ans += n - 1 + i;
        } else {
            ans += n - 1 + n - 1 - i;
        }
    }

    println!("{}", ans);
}
