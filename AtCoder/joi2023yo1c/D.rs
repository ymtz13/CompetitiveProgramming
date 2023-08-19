fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("");
    input
}

fn read_int_list() -> Vec<usize> {
    input()
        .split_whitespace()
        .map(|c| c.parse().expect(""))
        .collect()
}

fn main() {
    input();
    let a = read_int_list();

    for v in a.iter() {
        let mut ans = 0;

        for u in a.iter() {
            if u < v {
                ans += 1;
            }
        }

        println!("{}", ans + 1);
    }
}
