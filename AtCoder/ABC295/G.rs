fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn set(aa: &mut Vec<usize>, pp: &Vec<usize>, u: usize, v: usize) -> usize {
    if aa[u] <= v {
        return aa[u];
    }

    let p = if aa[u] == u { pp[u] } else { aa[u] };
    aa[u] = set(aa, pp, p, v);
    aa[u]
}

fn get(aa: &mut Vec<usize>, u: usize) -> usize {
    if aa[u] == u {
        return aa[u];
    }

    aa[u] = get(aa, aa[u]);
    aa[u]
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let mut pp = vec![0, 0];
    pp.extend(read_vec());
    let q: usize = read_line().parse().unwrap();
    let queries: Vec<_> = (0..q).map(|_| read_vec()).collect();

    let mut aa: Vec<_> = (0..=n).collect();

    for query in &queries {
        let t = query[0];
        if t == 1 {
            let u = query[1];
            let v = query[2];
            set(&mut aa, &pp, u, v);
        } else {
            let u = query[1];
            let ans = get(&mut aa, u);
            println!("{}", ans);
        }
    }
}
