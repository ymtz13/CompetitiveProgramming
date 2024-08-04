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
    let n: usize = read_line().parse().unwrap();
    let mut edges = vec![vec![]; n];
    let mut dd = vec![0; n];

    for _ in 1..n {
        let (a, b) = read_uu();
        edges[a].push(b);
        edges[b].push(a);
        dd[a] += 1;
        dd[b] += 1;
    }

    let mut stack = vec![];
    for i in 0..n {
        if dd[i] == 1 {
            stack.push(i);
        }
    }

    let mut ans = stack.len();

    let mut cnt = vec![0; n];

    while let Some(i) = stack.pop() {
        if dd[i] <= 2 && cnt[i] > 0 {
            continue;
        }
        cnt[i] += 1;

        if dd[i] <= 2 {
            for &j in &edges[i] {
                stack.push(j);
            }
        }
    }

    let mut m = 0;
    for i in 0..n {
        if dd[i] >= 3 {
            m += 1;
            if cnt[i] >= 1 {
                ans -= 1;
            }
        }
    }

    // println!("{dd:?}");
    // println!("{cnt:?}");

    let ans = if m == 0 { 1 } else { ans };
    println!("{ans}");
}
