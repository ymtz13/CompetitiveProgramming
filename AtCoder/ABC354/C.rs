fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let n: usize = read_line().parse().unwrap();

    let mut ca = vec![];
    for i in 1..=n {
        let ac = read_line();
        let mut ac = ac.split_whitespace();
        let a: usize = ac.next().unwrap().parse().unwrap();
        let c: usize = ac.next().unwrap().parse().unwrap();

        ca.push((c, a, i));
    }

    ca.sort();

    let mut ans = vec![];
    let mut amax = 0;

    for &(_, a, i) in &ca {
        if a > amax {
            amax = a;
            ans.push(i);
        }
    }
    ans.sort();

    let ans: Vec<_> = ans.into_iter().map(|i| i.to_string()).collect();

    println!("{}", ans.len());
    println!("{}", ans.join(" "));
}
