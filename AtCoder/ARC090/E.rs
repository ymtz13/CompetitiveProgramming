const MOD: usize = 1_000_000_007;

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

fn dijkstra(n: usize, edges: &Vec<Vec<(usize, i64)>>, s: usize) -> (Vec<i64>, Vec<usize>) {
    let inf = i64::MAX;

    let mut dist = vec![inf; n + 1];
    let mut cnt = vec![0; n + 1];
    cnt[s] = 1;

    let mut heap = std::collections::BinaryHeap::new();
    heap.push((0, s, 0));

    while let Some((d, q, from)) = heap.pop() {
        let d = -d;
        if dist[q] != inf && dist[q] != d {
            continue;
        }
        if from != 0 {
            cnt[q] += cnt[from];
            cnt[q] %= MOD;
        }
        if dist[q] != inf {
            continue;
        }
        dist[q] = d;

        for &(e, dd) in &edges[q] {
            heap.push((-(d + dd), e, q));
        }
    }

    (dist, cnt)
}

fn main() {
    let (n, m) = read_uu();
    let (s, t) = read_uu();

    let mut edges = vec![vec![]; n + 1];
    for _ in 0..m {
        let (u, v, d) = read_uuu();
        edges[u].push((v, 2 * d as i64));
        edges[v].push((u, 2 * d as i64));
    }

    let (dist_s, cnt_s) = dijkstra(n, &edges, s);
    let (dist_t, cnt_t) = dijkstra(n, &edges, t);

    // println!("{:?}", dist_s);
    // println!("{:?}", cnt_s);
    // println!("{:?}", dist_t);
    // println!("{:?}", cnt_t);

    let da = dist_s[t];
    let dx = da / 2;

    let mut ans = 0;

    for i in 1..=n {
        if dist_s[i] == dx && dist_t[i] == dx {
            // println!("{i} {} {}", cnt_s[i], cnt_t[i]);
            let c = cnt_s[i] * cnt_t[i] % MOD;
            ans += c * c % MOD;
            ans %= MOD;
        }
    }

    for i in 1..=n {
        for &(j, d) in &edges[i] {
            let ds = dist_s[i];
            let dt = dist_t[j];

            if ds < dx && dt < dx && ds + dt + d == da {
                let c = cnt_s[i] * cnt_t[j] % MOD;
                ans += c * c % MOD;
                ans %= MOD;
            }
        }
    }

    let ans = (MOD - ans + cnt_s[t] * cnt_s[t]) % MOD;
    println!("{ans}");
}
