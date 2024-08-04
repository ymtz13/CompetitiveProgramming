fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (i64, i64) {
    let v = read_vec();
    (v[0], v[1])
}

fn main() {
    let n = read_vec()[0] as usize;

    let mut s = 0;
    let mut ll = vec![];
    let mut rr = vec![];

    for _ in 0..n {
        let (l, r) = read_uu();
        s += l;
        ll.push(l);
        rr.push(r);
    }

    for i in 0..n {
        if s >= 0 {
            continue;
        }

        let v = std::cmp::min(-s, rr[i] - ll[i]);
        ll[i] += v;
        s += v;
    }

    if s != 0 {
        println!("No");
        return;
    }

    println!("Yes");

    let ans: Vec<_> = ll.iter().map(|v| v.to_string()).collect();

    println!("{}", ans.join(" "));
}
