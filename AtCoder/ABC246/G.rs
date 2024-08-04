fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (usize, usize) {
    let a = read_vec();
    (a[0], a[1])
}

fn dfs(i: usize, p: usize, tgt: usize, aa: &Vec<usize>, edges: &Vec<Vec<usize>>) -> i64 {
    let mut cnt = 0;

    for &e in &edges[i] {
        if e == p {
            continue;
        }

        if aa[e] >= tgt {
            cnt += 1;
        }
        cnt += dfs(e, i, tgt, &aa, &edges);
    }

    std::cmp::max(0, cnt - 1)
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let mut aa = vec![0, 0];
    aa.extend(read_vec());

    let mut edges = vec![vec![]; n + 1];
    for _ in 1..n {
        let (u, v) = read_uu();
        edges[u].push(v);
        edges[v].push(u);
    }

    let mut ok = 0;
    let mut ng = 1_000_000_001;

    while ng - ok > 1 {
        let tgt = (ng + ok) / 2;

        if dfs(1, 0, tgt, &aa, &edges) > 0 {
            ok = tgt;
        } else {
            ng = tgt;
        }
    }

    println!("{ok}");
}
