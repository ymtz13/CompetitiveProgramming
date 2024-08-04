fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_ii() -> (usize, usize) {
    let v = read_vec();
    (v[0], v[1])
}

fn main() {
    let (n, m) = read_ii();
    let tp: Vec<_> = (0..m).map(|_| read_ii()).collect();
    let q = read_vec()[0];
    let ab: Vec<_> = (0..q).map(|_| read_ii()).collect();

    let mut map = std::collections::HashMap::new();
    let mut rr = vec![];
    for i in 0..q {
        let j = map.entry(ab[i]).or_insert(i);
        rr.push(j.clone());
    }

    let mut degs = vec![0; n + 1];
    for i in 0..q {
        if i != rr[i] {
            continue;
        }
        let (a, b) = ab[i];
        degs[a] += 1;
        degs[b] += 1;
    }

    let mut edges = vec![vec![]; n + 1];
    for i in 0..q {
        if i != rr[i] {
            continue;
        }

        let (a, b) = ab[i];
        if degs[a] <= degs[b] {
            edges[a].push((b, i));
        } else {
            edges[b].push((a, i));
        }
    }

    let mut tt = vec![0; n + 1];
    let mut ss = vec![0; n + 1];
    let mut ans = vec![0i64; q];

    for &(t, p) in &tp {
        if tt[p] == 0 {
            tt[p] = t;

            for &(q, i) in &edges[p] {
                let s = ss[q] + if tt[q] == 0 { 0 } else { t - tt[q] };
                ans[i] -= s as i64;
            }
        } else {
            ss[p] += t - tt[p];
            tt[p] = 0;

            for &(q, i) in &edges[p] {
                let s = ss[q] + if tt[q] == 0 { 0 } else { t - tt[q] };
                ans[i] += s as i64;
            }
        }
    }

    for i in 0..q {
        let a = ans[rr[i]];
        println!("{a}");
    }
}
