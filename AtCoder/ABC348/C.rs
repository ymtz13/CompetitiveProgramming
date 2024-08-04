fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let mut pp = vec![];
    for _ in 0..n {
        let xy = read_vec();
        pp.push((xy[0], xy[1]));
    }

    let mut map = std::collections::HashMap::new();

    for (a, c) in pp.iter() {
        let v = map.entry(c).or_insert(a);
        if *v > a {
            *v = a;
        }
    }

    // println!("{:?}", map);

    let ans = map.iter().map(|(_, a)| a).max().unwrap();
    println!("{}", ans);
}
