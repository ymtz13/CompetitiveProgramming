use std::collections::{HashMap, VecDeque};

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
    let mut edges = vec![vec![]; n + 1];

    for _ in 0..n - 1 {
        let (u, v) = read_uu();
        edges[u].push(v);
        edges[v].push(u);
    }

    let aa = read_vec();

    let mut cnt = vec![0i64; n + 1];
    for &a in &aa {
        cnt[a] += 1;
    }

    let mut parent = vec![0; n + 1];
    let mut order = vec![];
    let mut queue = VecDeque::new();
    queue.push_back((1, 0));

    while let Some((i, p)) = queue.pop_front() {
        parent[i] = p;
        order.push(i);
        for &j in &edges[i] {
            if j != p {
                queue.push_back((j, i));
            }
        }
    }

    let mut maps = vec![HashMap::new()];
    let mut ss = vec![0];

    for i in 1..=n {
        let a = aa[i - 1];
        maps.push(HashMap::from([(a, 1)]));
        ss.push(cnt[a] - 1);
    }

    let mut ans = 0;
    for &i in order.iter().rev() {
        if i == 1 {
            break;
        }

        let mut s = ss[i];
        let mut xx = vec![(n - 1, i)];
        for &j in &edges[i] {
            if j == parent[i] {
                continue;
            }
            // println!("i: {i}, j: {j}");
            s += ss[j];
            xx.push((n - maps[j].len(), j));
        }

        xx.sort();

        let p0 = xx[0].1;
        for &(_, p) in &xx[1..] {
            let mut kvpair = vec![];
            for (&key, &val) in maps[p].iter() {
                let c = cnt[key];
                if let Some(val0) = maps[p0].get(&key) {
                    s -= val0 * (c - val0) + val * (c - val);
                    let valt = val0 + val;
                    s += valt * (c - valt);
                    kvpair.push((key, valt));
                } else {
                    kvpair.push((key, val));
                }
            }

            for &(key, val) in &kvpair {
                maps[p0].insert(key, val);
            }
        }

        // *maps.get_mut(i).unwrap() = *maps.get(p0).unwrap();
        maps.swap(i, p0);
        ss[i] = s;

        // println!("i: {i}, map: {:?}", maps[i]);

        ans += ss[i];
    }

    // println!("{ss:?}");

    println!("{ans}");
}
