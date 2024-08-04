fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    read_line();
    let aa = read_vec();

    let mut min = 2;
    let mut max = 2;
    for &a in aa.iter().rev() {
        let min_nxt = (min + a - 1) / a * a;
        let max_nxt = max / a * a + a - 1;

        min = min_nxt;
        max = max_nxt;

        if min > max {
            println!("-1");
            return;
        }
    }

    println!("{min} {max}");
}
