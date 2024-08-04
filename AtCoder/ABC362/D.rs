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

fn read_uuu() -> (usize, usize, usize) {
    let v = read_vec();
    (v[0], v[1], v[2])
}

fn main() {
    let (n, m) = read_uu();
    let aa = read_vec();

    let mut edges = vec![vec![]; 2 * n + 1];
    for i in 1..=n {
        edges[i].push((n + i, aa[i - 1] as i64));
    }
    for _ in 0..m {
        let (u, v, b) = read_uuu();
        edges[n + u].push((v, b as i64));
        edges[n + v].push((u, b as i64));
    }

    let mut heap = std::collections::BinaryHeap::new();
    heap.push((0, 1));
    let mut dist = vec![i64::MAX; 2 * n + 1];

    while let Some((d, i)) = heap.pop() {
        if dist[i] != i64::MAX {
            continue;
        }
        dist[i] = -d;

        for &(j, w) in &edges[i] {
            heap.push((d - w, j));
        }
    }

    let mut ans = vec![];
    for i in 2..=n {
        ans.push(dist[n + i].to_string());
    }

    println!("{}", ans.join(" "));
}
