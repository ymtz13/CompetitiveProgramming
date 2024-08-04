fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uuu() -> (usize, usize, usize) {
    let v = read_vec();
    (v[0], v[1], v[2])
}

fn solve(ee: &Vec<(usize, usize, usize)>) -> Vec<i64> {
    let mut edges = vec![vec![]; 302];
    let mut caps = vec![];

    let inf = i64::MAX >> 1;

    let s = 0;
    let a0 = 0;
    let b0 = 150;
    let t = 301;

    for i in 1..=150 {
        edges[s].push((a0 + i, caps.len()));
        caps.push(0);
        edges[a0 + i].push((s, caps.len()));
        caps.push(0);

        edges[b0 + i].push((t, caps.len()));
        caps.push(0);
        edges[t].push((b0 + i, caps.len()));
        caps.push(0);
    }

    for &(a, b, c) in ee {
        edges[a0 + a].push((b0 + b, caps.len()));
        caps.push(c as i64);
        edges[b0 + b].push((a0 + a, caps.len()));
        caps.push(0);
    }

    let mut ret = vec![];

    loop {
        let mut heap = std::collections::BinaryHeap::new();
        heap.push((inf, s, (0, 0)));

        let mut amt = vec![0; 302];
        let mut from = vec![None; 302];
        while let Some((v, i, (f, p))) = heap.pop() {
            if from[i].is_some() {
                continue;
            }
            amt[i] = v;
            from[i] = Some((f, p));

            for &(j, p) in &edges[i] {
                let cap = caps[p];
                let w = std::cmp::min(cap, v);
                if w > 0 {
                    heap.push((w, j, (i, p)));
                }
            }
        }

        let v = amt[t];
        if v == 0 {
            break;
        }

        ret.push(v);

        println!("---{:?}---", v);

        let mut i = t;
        while i != s {
            let (f, p) = from[i].unwrap();
            let q = p ^ 1;
            println!("{f} --> {i}");

            caps[p] -= v;
            caps[q] += v;

            i = f;
        }
    }

    return ret;
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let mut ee = vec![];
    for _ in 0..n {
        ee.push(read_uuu());
    }

    let ans = solve(&ee);
    println!("{ans:?}");
}
