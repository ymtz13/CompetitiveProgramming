use std::cmp::min;

const MOD: usize = 998244353;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_uu() -> (usize, usize) {
    let s = read_line();
    let mut iter = s.split_whitespace().map(|c| c.parse().unwrap());
    (iter.next().unwrap(), iter.next().unwrap())
}

fn dfs(i: usize, edges: &Vec<Vec<usize>>, p: usize) -> (Vec<usize>, Vec<usize>) {
    let mut vv0 = vec![1, 0];
    let mut vv1 = vec![0, 1];

    for &j in &edges[i] {
        if j == p {
            continue;
        }

        let (ww0, ww1) = dfs(j, &edges, i);

        let ni = vv0.len() - 1;
        let nj = ww0.len() - 1;
        let n = ni + nj;

        let mut vv0_nxt = vec![0; n + 1];
        let mut vv1_nxt = vec![0; n + 1];

        for m in 0..=n {
            let k0 = if m > nj { m - nj } else { 0 };
            for k in k0..=min(ni, m) {
                vv0_nxt[m] += vv0[k] * (ww0[m - k] + ww1[m - k]);
                vv0_nxt[m] %= MOD;
            }

            let k0 = if m + 1 > nj { m + 1 - nj } else { 0 };
            for k in k0..=min(ni, m) {
                vv1_nxt[m] += vv1[k] * (ww0[m - k] + ww1[m - k + 1]);
                vv1_nxt[m] %= MOD;
            }
        }

        vv0 = vv0_nxt;
        vv1 = vv1_nxt;
    }

    (vv0, vv1)
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let mut edges = vec![vec![]; n + 1];

    for _ in 0..n - 1 {
        let (u, v) = read_uu();
        edges[u].push(v);
        edges[v].push(u);
    }

    let (vv0, vv1) = dfs(1, &edges, 0);

    for x in 1..=n {
        let ans = (vv0[x] + vv1[x]) % MOD;
        println!("{ans}");
    }
}
