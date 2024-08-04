fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn solve(n: usize, edges: &Vec<Vec<(usize, i64)>>) -> usize {
    let null = 2;

    use std::collections::VecDeque;
    let mut queue = VecDeque::from(vec![(1, 1, 0)]);
    let mut values = vec![0; n + 1];
    let mut parities = vec![null; n + 1];
    let mut odd_cycle = None;
    while let Some(tup) = queue.pop_back() {
        let (q, v, p) = tup;
        if parities[q] != null {
            if parities[q] == p && values[q] != v {
                eprintln!("{:?}", (1, q, v, p));
                return 0;
            }
            if parities[q] != p {
                if (values[q] - v) % 2 != 0 {
                    eprintln!("{:?}", (2, q, v, p));
                    return 0;
                }
                odd_cycle = Some((q, (values[q] + v) / 2));
            }

            continue;
        }
        values[q] = v;
        parities[q] = p;

        for &(e, s) in &edges[q] {
            queue.push_front((e, s - v, 1 - p));
        }
    }

    eprintln!("{:?}", odd_cycle);

    if let Some((q0, v0)) = odd_cycle {
        let mut queue = VecDeque::from(vec![(q0, v0)]);
        let mut values = vec![0; n + 1];
        let mut visited = vec![false; n + 1];
        while let Some(tup) = queue.pop_back() {
            let (q, v) = tup;
            if visited[q] {
                if values[q] != v {
                    eprintln!("{:?}", (3, q, v, values));
                    return 0;
                }
                continue;
            }
            values[q] = v;
            visited[q] = true;
            if v <= 0 {
                return 0;
            }

            for &(e, s) in &edges[q] {
                queue.push_front((e, s - v));
            }
        }
        eprintln!("{:?}", values);

        return 1;
    } else {
        let mut min_p0 = 1 << 60;
        let mut min_p1 = 1 << 60;
        use std::cmp::min;
        for i in 1..=n {
            if parities[i] == 0 {
                min_p0 = min(min_p0, values[i]);
            } else {
                min_p1 = min(min_p1, values[i]);
            }
        }
        let ret = min_p0 + min_p1 - 1;
        return if ret >= 0 { ret as usize } else { 0 };
    }
}

fn main() {
    let nm = read_vec();
    let n = nm[0];
    let m = nm[1];

    let mut edges = vec![vec![]; n + 1];
    for _ in 0..m {
        let uvs = read_vec();
        let u = uvs[0];
        let v = uvs[1];
        let s = uvs[2] as i64;

        edges[u].push((v, s));
        edges[v].push((u, s));
    }

    let ans = solve(n, &edges);

    println!("{}", ans);
}
