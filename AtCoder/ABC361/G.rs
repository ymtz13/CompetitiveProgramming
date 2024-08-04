fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (usize, usize) {
    let v = read_vec();
    (v[0], v[1])
}

fn main() {
    let n = read_vec()[0];
    let w = 1 << 18;

    let mut set = std::collections::HashSet::new();
    for _ in 0..n {
        let (x, y) = read_uu();
        set.push(((x + 1) << 18) + y + 1);
    }

    let mut map = std::collections::HashMap::new();
    let mut queue = std::collections::VecDeque::new();

    for &xy in &set {
        let x = xy >> 18;
        let y = xy & mask;
    }
}
