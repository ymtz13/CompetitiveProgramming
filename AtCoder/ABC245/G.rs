fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uuuu() -> (usize, usize, usize, usize) {
    let v = read_vec();
    (v[0], v[1], v[2], v[3])
}

fn read_uuu() -> (usize, usize, usize) {
    let v = read_vec();
    (v[0], v[1], v[2])
}

fn main() {
    let (n, m, k, l) = read_uuuu();
    let aa = read_vec();
    let bb = read_vec();

    let mut edges = vec![vec![]; n + 1];
    for _ in 0..m {
        let (u, v, c) = read_uuu();
        edges[u].push((v, c as i64));
        edges[v].push((u, c as i64));
    }

    let mut heap = std::collections::BinaryHeap::new();
    for &b in &bb {
        heap.push((0i64, b, aa[b - 1]));
    }

    let mut dist1 = vec![(0, 0); n + 1];
    let mut dist2 = vec![(0, 0); n + 1];

    while let Some((d, i, a)) = heap.pop() {
        if dist1[i].1 == 0 {
            dist1[i] = (-d, a);
        } else if dist2[i].1 == 0 && dist1[i].1 != a {
            dist2[i] = (-d, a);
        } else {
            continue;
        }

        for &(j, c) in &edges[i] {
            heap.push((d - c, j, a));
        }
    }

    let mut ans = vec![String::from("-1"); n];
    for i in 1..=n {
        let a = aa[i - 1];
        let (d1, a1) = dist1[i];
        let (d2, a2) = dist2[i];
        if a1 != 0 && a1 != a {
            ans[i - 1] = d1.to_string();
        } else if a2 != 0 && a2 != a {
            ans[i - 1] = d2.to_string();
        }
    }

    println!("{}", ans.join(" "));
}
