fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn gcd(mut a: usize, mut b: usize) -> usize {
    while a % b > 0 {
        (a, b) = (b, a % b);
    }
    b
}

fn main() {
    let nm: Vec<usize> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    let n = nm[0];
    let m = nm[1];

    let s = read_line().into_bytes();
    let t = read_line().into_bytes();

    let lcd = n * m / gcd(n, m);

    let mut vv = std::collections::HashMap::new();
    for i in 0..n {
        vv.insert(i * lcd / n, s[i]);
    }
    for i in 0..m {
        let key = i * lcd / m;
        if vv.get(&key).is_some_and(|&v| v != t[i]) {
            println!("-1");
            return;
        }
    }

    println!("{lcd}");
}
