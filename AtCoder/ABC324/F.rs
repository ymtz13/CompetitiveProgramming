fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("");
    input
}

fn read_int_vec() -> Vec<usize> {
    input()
        .split_whitespace()
        .map(|c| c.parse().expect(""))
        .collect()
}

fn main() {
    let nm = read_int_vec();
    let n = nm[0];
    let m = nm[1];

    let mut e = vec![vec![]; n];

    for _ in 0..m {
        let uvbc = read_int_vec();
        let u = uvbc[0];
        let v = uvbc[1];
        let b = uvbc[2];
        let c = uvbc[3];

        e[u].push((v, b as f64, c as f64));
    }

    let mut ok = 0.0;
    let mut ng = 10001.0;

    let inf = 1e10;

    while (ng - ok) > 1e-10 {
        let tgt = (ng + ok) / 2.0;

        let mut dp = vec![-inf; n + 1];
        dp[1] = 0.0;

        for f in 1..n {
            let v = dp[f];

            for (t, b, c) in e[f].iter() {
                let z = v + b - tgt * c;
                if dp[*t] < z {
                    dp[*t] = z;
                }
            }
        }

        if dp[n] >= 0.0 {
            ok = tgt;
        } else {
            ng = tgt;
        }
    }

    println!("{:?}", ok);
}
