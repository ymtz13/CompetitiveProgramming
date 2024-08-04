fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let n = read_vec()[0];
    let hh = read_vec();

    let mut s = 0;
    let mut i = 0;
    let mut stack_h = vec![usize::MAX; n + 1];
    let mut stack_x = vec![0; n + 1];

    let mut ans = vec![];

    for &h in &hh {
        let mut x = 1;
        while stack_h[i] < h {
            x += stack_x[i];
            s -= stack_h[i] * stack_x[i];
            i -= 1;
        }
        i += 1;
        stack_h[i] = h;
        stack_x[i] = x;
        s += h * x;

        ans.push((s + 1).to_string());
    }

    println!("{}", ans.join(" "));
}
