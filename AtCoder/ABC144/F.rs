fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_uu() -> (usize, usize) {
    let vec: Vec<_> = read_line().split_whitespace().map(|v| v.parse().unwrap()).collect();
    (vec[0], vec[1])
}

fn main() {
    let (n, m) = read_uu();

    let mut edges_f = vec![vec![]; n];
    let mut edges_b = vec![vec![]; n];
    let mut deg_f = vec![0; n];
    let mut edges = vec![];

    for _ in 0..m {
        let (mut s, mut t) = read_uu();
        s -= 1;
        t -= 1;

        edges_f[s].push(t);
        edges_b[t].push(s);
        deg_f[s] += 1;
        edges.push((s, t));
    }

    let mut prob = vec![0.0; n];
    let mut expt_f = vec![0.0; n];
    prob[0] = 1.0;

    for i in 1..n {
        for &j in &edges_b[i] {
            prob[i] += prob[j] * (1.0 / deg_f[j] as f64);
        }

        for &j in &edges_b[i] {
            let p = prob[j] * (1.0 / deg_f[j] as f64) / prob[i];
            expt_f[i] += (expt_f[j] + 1.0) * p;
        }
    }

    // println!("{:?}", prob);
    // println!("{:?}", expt_f);

    let mut expt_b = vec![0.0; n];
    for i in (0..n - 1).rev() {
        for &j in &edges_f[i] {
            expt_b[i] += expt_b[j] / deg_f[i] as f64;
        }
        expt_b[i] += 1.0;
    }
    // println!("{:?}", expt_b);

    let e0 = expt_b[0];
    let mut ans = e0;

    // println!("e0={}", e0);
    for &(s, t) in &edges {
        let deg = deg_f[s];
        if deg == 1 {
            continue;
        }

        let deg = deg as f64;
        let v0 = expt_b[s];
        let v1 = ((expt_b[s] - 1.0) * deg - expt_b[t]) / (deg - 1.0) + 1.0;
        let gain = v0 - v1;
        let p = prob[s];
        let a = e0 - p * gain;
        // println!("{:?}", ((s, t), p, (v0, v1), gain, e0 - p * gain));

        // let e = 1.0 + expt_f[s] + expt_b[t];
        // let p = prob[s] / (deg as f64);
        // let b = e0 - e * p;
        // let a = b / (1.0 - p);

        // println!("{:?}", ((s, t), e, p, b, a));
        if a < ans {
            ans = a;
        }
    }

    println!("{}", ans);

    // println!("{:?}", edges_f);
}
