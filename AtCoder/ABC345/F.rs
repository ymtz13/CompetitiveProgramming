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

fn read_uu() -> (usize, usize) {
    let v = read_vec();
    (v[0], v[1])
}

fn dfs(edges: &Vec<Vec<(usize, usize)>>, xx: &mut Vec<usize>, ans: &mut Vec<String>, visited: &mut Vec<bool>, i: usize, k: usize) -> usize {
    visited[i] = true;

    let mut kk = k;
    let mut jj = vec![];

    for &(j, l) in &edges[i] {
        if visited[j] {
            continue;
        }
        jj.push((j, l));
        kk -= dfs(edges, xx, ans, visited, j, kk);
    }

    // println!("{i} {jj:?} {k} {kk}");

    for &(j, l) in &jj {
        if kk == 0 {
            break;
        }
        if xx[j] == 1 {
            continue;
        }

        ans.push(l.to_string());

        if xx[i] == 0 {
            xx[i] = 1;
            kk -= 2;
        } else {
            xx[i] = 0;
        }
    }

    k - kk
}

fn main() {
    let (n, m, k) = read_uuu();
    let mut edges = vec![vec![]; n + 1];

    for i in 1..=m {
        let (u, v) = read_uu();
        edges[u].push((v, i));
        edges[v].push((u, i));
    }

    if k % 2 == 1 {
        println!("No");
        return;
    }

    let mut visited = vec![false; n + 1];
    let mut xx = vec![0; n + 1];
    let mut ans = vec![];
    let mut kk = k;
    for r in 1..=n {
        if visited[r] {
            continue;
        }

        kk -= dfs(&edges, &mut xx, &mut ans, &mut visited, r, kk);
        // println!("*** {kk} {visited:?}");
    }

    if kk == 0 {
        println!("Yes");
        println!("{}", ans.len());
        println!("{}", ans.join(" "));
    } else {
        println!("No");
    }
}
