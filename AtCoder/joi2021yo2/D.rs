fn read_int_vec<T: std::str::FromStr>() -> Vec<T>
where
    <T as std::str::FromStr>::Err: std::fmt::Debug,
{
    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();

    inp.trim()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect()
}

fn f(n: usize, k: usize, time: i64, avec: &Vec<i64>, bvec: &Vec<i64>) -> bool {
    let mut cvec = bvec.clone();
    let mut i = 0;

    for _ in 0..k {
        let mut t = time - avec[i];
        while t > 0 {
            let c = std::cmp::min(cvec[i], t);
            cvec[i] -= c;
            t -= c;
            if cvec[i] == 0 {
                if i == n - 1 {
                    return true;
                }
                t -= avec[i + 1] - avec[i];
                i += 1;
            }
        }
    }

    false
}

fn main() {
    let nk = read_int_vec::<usize>();
    let n = nk[0];
    let k = nk[1];

    let avec = read_int_vec::<i64>();
    let bvec = read_int_vec::<i64>();

    let mut ok = 1 << 50;
    let mut ng = 0;

    while ok - ng > 1 {
        let tgt = (ok + ng) / 2;
        if f(n, k, tgt, &avec, &bvec) {
            ok = tgt
        } else {
            ng = tgt
        }
    }

    println!("{}", ok);
}
