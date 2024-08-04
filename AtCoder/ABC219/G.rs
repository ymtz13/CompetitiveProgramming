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

fn main() {
    let (n, m, q) = read_uuu();
    let mut edges = vec![vec![]; n + 1];
    let mut fedges = vec![vec![]; n + 1];

    let d0 = 600;

    for _ in 0..m {
        let (u, v) = read_uu();
        edges[u].push(v);
        edges[v].push(u);
    }

    for t in 1..=n {
        for &f in &edges[t] {
            if edges[f].len() > d0 {
                fedges[t].push(f);
            }
        }
    }

    let mut vl: Vec<_> = (0..=n).collect();
    let mut ut = vec![0; n + 1];
    let mut pr = vec![0; n + 1];
    let mut pt = vec![0; n + 1];

    let xx = read_vec();
    for i in 1..=q {
        let x = xx[i - 1];
        let d = edges[x].len();

        for &f in &fedges[x] {
            if pt[f] > ut[x] {
                vl[x] = pr[f];
                ut[x] = pt[f];
            }
        }

        pr[x] = vl[x];
        pt[x] = i;

        if d <= d0 {
            for &e in &edges[x] {
                vl[e] = vl[x];
                ut[e] = i;
            }
        }
    }

    for x in 1..=n {
        for &f in &fedges[x] {
            if pt[f] > ut[x] {
                vl[x] = pr[f];
                ut[x] = pt[f];
            }
        }
    }

    let ans: Vec<_> = vl[1..].iter().map(|v| v.to_string()).collect();
    println!("{}", ans.join(" "));
}
