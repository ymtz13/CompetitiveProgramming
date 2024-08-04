fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn read_uu() -> (usize, usize) {
    let v = read_vec();
    (v[0], v[1])
}

fn solve(n: usize, edges: &Vec<Vec<usize>>, queue: Vec<(usize, usize)>) -> usize {
    let mut dist = vec![usize::MAX; n + 1];
    let mut queue = std::collections::VecDeque::from(queue);

    while let Some((i, d)) = queue.pop_front() {
        if dist[i] < usize::MAX {
            continue;
        }
        dist[i] = d;
        for &j in &edges[i] {
            queue.push_back((j, d + 1));
        }
    }

    let mut cnt = vec![0; n + 1];
    let mut degmax = vec![0; n + 1];

    for i in 1..=n {
        let d = dist[i];
        cnt[d] += 1;
        degmax[d] = std::cmp::max(degmax[d], edges[i].len() - 1);
    }

    for d in 1..n {
        cnt[d + 1] = cnt[d] * degmax[d];
    }

    *cnt.iter().max().unwrap()
}

fn main() {
    let n = read_vec()[0];
    let mut edges = vec![vec![]; n + 1];
    for _ in 0..n - 1 {
        let (a, b) = read_uu();
        edges[a].push(b);
        edges[b].push(a);
    }

    let mut dist = vec![usize::MAX; n + 1];
    let mut queue = std::collections::VecDeque::from(vec![(1, 0)]);
    while let Some((i, d)) = queue.pop_front() {
        if dist[i] < usize::MAX {
            continue;
        }
        dist[i] = d;
        for &j in &edges[i] {
            queue.push_back((j, d + 1));
        }
    }

    // println!("{dist:?}");

    let mut dmax = 0;
    let mut r = 0;
    for i in 1..=n {
        if dist[i] > dmax {
            dmax = dist[i];
            r = i;
        }
    }

    let mut dist = vec![usize::MAX; n + 1];
    let mut prev = vec![usize::MAX; n + 1];
    let mut queue = std::collections::VecDeque::from(vec![(r, 0, 0)]);
    while let Some((i, d, p)) = queue.pop_front() {
        if dist[i] < usize::MAX {
            continue;
        }
        dist[i] = d;
        prev[i] = p;
        for &j in &edges[i] {
            queue.push_back((j, d + 1, i));
        }
    }

    // println!("{dist:?}");
    // println!("{prev:?}");

    let mut dmax = 0;
    let mut s = 0;
    for i in 1..=n {
        if dist[i] > dmax {
            dmax = dist[i];
            s = i;
        }
    }

    // println!("{dmax} {s}");

    let mut i = s;
    let mut diam = vec![];
    while i != 0 {
        diam.push(i);
        i = prev[i];
    }
    let l = diam.len();

    // println!("{diam:?}");

    let mut ans;

    if l % 2 == 0 {
        ans = solve(n, &edges, vec![(diam[l / 2 - 1], 1), (diam[l / 2], 1)]);
    } else {
        let root = diam[l / 2];
        ans = solve(n, &edges, vec![(root, 0)]);
        for &j in &edges[root] {
            ans = std::cmp::min(ans, solve(n, &edges, vec![(root, 1), (j, 1)]));
        }
    }

    println!("{} {}", (l + 1) / 2, ans);
}
