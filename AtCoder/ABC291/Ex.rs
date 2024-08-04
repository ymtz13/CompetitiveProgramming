use std::collections::HashSet;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_uu() -> (usize, usize) {
    let uu: Vec<_> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    (uu[0], uu[1])
}

fn center(edges: &Vec<Vec<usize>>, verts: &HashSet<usize>, i: usize, parent: usize) -> (usize, Option<usize>) {
    let mut sum = 1;
    let mut max = 0;
    for &j in &edges[i] {
        if j == parent || !verts.contains(&j) {
            continue;
        }
        let (m, ret) = center(edges, verts, j, i);

        if ret.is_some() {
            return (0, ret);
        }

        if m > max {
            max = m;
        }

        sum += m;
    }

    if verts.len() - sum > max {
        max = verts.len() - sum;
    }

    if max * 2 <= verts.len() {
        return (0, Some(i));
    }

    (sum, None)
}

fn connected(edges: &Vec<Vec<usize>>, verts: &HashSet<usize>, i: usize, parent: usize, ret: &mut HashSet<usize>) {
    if !verts.contains(&i) {
        return;
    }
    ret.insert(i);

    for &j in &edges[i] {
        if j == parent || !verts.contains(&j) {
            continue;
        }
        connected(edges, verts, j, i, ret);
    }
}

fn solve(edges: &Vec<Vec<usize>>, verts: &HashSet<usize>, parent: usize, ans: &mut Vec<usize>) {
    let &r = verts.iter().next().unwrap();

    if verts.len() == 1 {
        ans[r] = parent;
        return;
    }

    let c = center(edges, verts, r, parent);
    let c = c.1.unwrap();
    ans[c] = parent;

    for &j in &edges[c] {
        if !verts.contains(&j) {
            continue;
        }

        let mut connected_verts = HashSet::new();
        connected(edges, verts, j, c, &mut connected_verts);
        solve(edges, &connected_verts, c, ans);
    }
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let mut edges = vec![vec![]; n + 1];
    for _ in 0..n - 1 {
        let (a, b) = read_uu();
        edges[a].push(b);
        edges[b].push(a);
    }

    let mut ans = vec![0; n + 1];
    solve(&edges, &((1..=n).collect()), 0, &mut ans);

    let ans: Vec<i64> = ans[1..].iter().map(|&c| if c > 0 { c as i64 } else { -1 }).collect();
    let ans: Vec<_> = ans.iter().map(|c| c.to_string()).collect();

    println!("{}", ans.join(" "));
}
