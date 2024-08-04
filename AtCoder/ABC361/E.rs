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

fn main() {
    let n = read_vec()[0];
    let mut edges = vec![vec![]; n + 1];
    let mut s = 0;
    for _ in 0..n - 1 {
        let (a, b, c) = read_uuu();
        edges[a].push((b, c));
        edges[b].push((a, c));
        s += c * 2;
    }

    use std::collections::VecDeque;

    let mut dist = vec![usize::MAX; n + 1];
    let mut queue = VecDeque::new();
    queue.push_back((1, 0));
    while let Some((i, d)) = queue.pop_front() {
        if dist[i] != usize::MAX {
            continue;
        }
        dist[i] = d;

        for &(j, dd) in &edges[i] {
            queue.push_back((j, d + dd));
        }
    }

    let mut root = 1;
    for i in 2..=n {
        if dist[i] > dist[root] {
            root = i;
        }
    }

    // println!("{dist:?} {root}");

    let mut dist = vec![usize::MAX; n + 1];
    let mut queue = VecDeque::new();
    queue.push_back((root, 0));
    while let Some((i, d)) = queue.pop_front() {
        if dist[i] != usize::MAX {
            continue;
        }
        dist[i] = d;

        for &(j, dd) in &edges[i] {
            queue.push_back((j, d + dd));
        }
    }

    let mut maxd = 0;
    for i in 1..=n {
        if dist[i] > maxd {
            maxd = dist[i];
        }
    }

    let ans = s - maxd;

    println!("{ans}");
}
