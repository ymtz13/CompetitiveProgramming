use std::collections::HashMap;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn dfs(memo: &mut HashMap<(usize, usize), (usize, usize)>, edges: &Vec<Vec<usize>>, cc: &Vec<usize>, p: usize, i: usize) -> (usize, usize) {
    if let Some(&ret) = memo.get(&(p, i)) {
        return ret;
    }

    let mut v = cc[i];
    let mut s = cc[i];

    for &e in edges[i].iter() {
        if e == p {
            continue;
        }

        let (ve, se) = dfs(memo, edges, cc, i, e);
        s += se;
        v += ve + se;
    }

    let ret = (v, s);
    memo.insert((p, i), ret);
    return ret;
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let mut pp = vec![];
    let mut edges = vec![vec![]; n];
    for _ in 0..n - 1 {
        let xy = read_vec();
        let x = xy[0] - 1;
        let y = xy[1] - 1;
        pp.push((x, y));
        edges[x].push(y);
        edges[y].push(x);
    }

    let cc = read_vec();

    let mut memo = HashMap::new();

    let mut ans = vec![0; n];
    for &(a, b) in &pp {
        let va = dfs(&mut memo, &edges, &cc, a, b).0;
        let vb = dfs(&mut memo, &edges, &cc, b, a).0;
        ans[a] += va;
        ans[b] += vb;
    }

    // println!("{:?}", memo);
    // println!("{:?}", ans);

    println!("{}", ans.iter().min().unwrap());
}
