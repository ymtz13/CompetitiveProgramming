fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let n: usize = read_line().parse().unwrap();

    let mut sum = 0;
    let mut names = vec![];

    for _ in 0..n {
        let sc = read_line();
        let mut sc = sc.split_whitespace();
        names.push(sc.next().unwrap().to_string());

        let c: usize = sc.next().unwrap().parse().unwrap();
        sum += c;
    }

    names.sort();

    println!("{}", names[sum % n]);
}
