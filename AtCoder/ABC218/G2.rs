fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let n: usize = read_line().parse().unwrap();

    let mut aa = vec![0];
    aa.extend(read_vec());
    let aa = aa;

    let mut edges = vec![vec![]; n + 1];
    for _ in 0..n - 1 {
        let uv = read_vec();
        let u = uv[0] as usize;
        let v = uv[1] as usize;

        edges[u].push(v);
        edges[v].push(u);
    }

    let inf = n + 10;

    use std::collections::VecDeque;
    let mut queue = VecDeque::from(vec![(1, 0)]);
    let mut depth = vec![inf; n + 1];
    let mut order = vec![];
    while let Some((i, d)) = queue.pop_back() {
        if depth[i] != inf {
            continue;
        }
        depth[i] = d;
        order.push(i);

        for &j in &edges[i] {
            queue.push_front((j, d + 1));
        }
    }

    println!("{depth:?}");
    println!("{order:?}");

    let mut ok = 2;
    let mut ng = 1_000_000_001;

    while ng - ok > 1 {
        let tgt = (ok + ng) / 2;

        let mut ss = vec![0; n + 1];

        for &i in order.iter().rev() {
            let d = depth[i];

            let mut cc = vec![];
            for &j in &edges[i] {
                if depth[j] < d {
                    continue;
                }

                cc.push(ss[j]);
            }
            cc.sort();

            ss[i] = if aa[i] >= tgt { 1 } else { -1 };

            if cc.len() > 0 {
                if d % 2 == 0 {
                    ss[i] += cc.iter().max().unwrap();
                } else {
                    ss[i] += cc.iter().min().unwrap();
                }
            }
        }

        if ss[1] >= 0 {}
    }

    println!("{ok}");
}
