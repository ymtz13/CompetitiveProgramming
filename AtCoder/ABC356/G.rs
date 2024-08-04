fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_ii() -> (i128, i128) {
    let v = read_line();
    let v: Vec<_> = v.split_whitespace().map(|c| c.parse().unwrap()).collect();
    (v[0], v[1])
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let mut ab = vec![];
    for _ in 0..n {
        ab.push(read_ii());
    }

    ab.sort();
    ab.reverse();

    // println!("{ab:?}");

    let mut a_prev = 0;
    let mut ab_dedup = vec![(0, 0)];
    for &(a, b) in &ab {
        if a == a_prev {
            continue;
        }
        ab_dedup.push((a, b));
        a_prev = a;
    }

    let ab = ab_dedup;
    // println!("{ab:?}");

    let m = ab.len() - 1;

    let mut zz: Vec<_> = (1..=m).collect();

    for i in (0..m).rev() {
        while zz[i] < m {
            let j = zz[i];
            let k = zz[j];

            let (ai, bi) = ab[i];
            let (aj, bj) = ab[j];
            let (ak, bk) = ab[k];

            let nr = aj * bk - ak * bj;
            let dr = aj - ak;
            let nl;
            let dl;

            if ai == 0 {
                nl = bj;
                dl = 1;
            } else {
                nl = ai * bj - aj * bi;
                dl = ai - aj;
            }

            if nl * dr > nr * dl {
                break;
            }

            zz[i] = k;
        }
    }

    let mut cc = vec![(0, 0)];

    let mut i = 0;
    while i < m {
        i = zz[i];

        let (a, b) = ab[i];
        let (al, bl) = cc[cc.len() - 1];

        if al == 0 || bl * a < b * al {
            cc.push((a, b));
        }
    }

    // println!("zz:{zz:?}");
    // println!("cc:{cc:?}");

    let (al, bl) = cc[cc.len() - 1];

    let q: usize = read_line().parse().unwrap();
    let mut cd = vec![];
    for _ in 0..q {
        cd.push(read_ii());
    }

    for &(c, d) in &cd {
        if bl * c < al * d {
            println!("-1");
            continue;
        }

        let mut l = 0;
        let mut r = cc.len() - 1;
        while r - l > 1 {
            let tgt = (l + r) / 2;

            let (a, b) = cc[tgt];
            if b * c < a * d {
                l = tgt;
            } else {
                r = tgt;
            }
        }

        let (a0, b0) = cc[l];
        let (a1, b1) = cc[r];

        if a0 == 0 {
            let ans = (d as f64) / (b1 as f64);
            println!("{ans}");
        } else {
            let p = d * (a0 - a1) + c * (b1 - b0);
            let q = a0 * b1 - a1 * b0;
            let ans = (p as f64) / (q as f64);
            println!("{ans}");
        }
    }
}
