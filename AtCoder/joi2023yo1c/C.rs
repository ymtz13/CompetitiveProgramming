fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("");
    input
}

fn main() {
    input();
    let s = input();
    let s = s.trim();

    let mut prev = ' ';
    let mut ans = String::new();

    for c in s.chars() {
        if prev == c {
            let upper = c.to_ascii_uppercase();
            ans.push(upper);
            ans.push(upper);
            prev = ' ';
        } else {
            if prev != ' ' {
                ans.push(prev);
            }
            prev = c;
        }
        println!("{c}");
    }

    if prev != ' ' {
        ans.push(prev);
    }

    println!("{}", ans);
}
