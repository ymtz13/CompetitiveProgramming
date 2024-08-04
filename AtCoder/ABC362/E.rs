const MOD: usize = 998244353;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (i64, i64) {
    let v = read_vec();
    (v[0], v[1])
}

fn main() {
    let n = read_vec()[0] as usize;
    let aa = read_vec();

    let mut dp: Vec<std::collections::HashMap<i64, Vec<usize>>> = vec![];

    for i in 0..n {
        let ai = aa[i];
        let mut map = std::collections::HashMap::new();

        for j in 0..i {
            let aj = aa[j];
            let d = ai - aj;
            let mut vv = map.entry(d).or_insert(vec![0; n + 1]);
            vv[2] += 1;
            vv[2] %= MOD;

            if let Some(vvj) = dp[j].get(&d) {
                for k in 3..=n {
                    vv[k] += vvj[k - 1];
                    vv[k] %= MOD;
                }
            }
        }

        dp.push(map);
    }

    let mut ans = vec![0; n + 1];
    ans[1] = n;
    for map in &dp {
        for vv in map.values() {
            for k in 2..=n {
                ans[k] += vv[k];
                ans[k] %= MOD;
            }
        }
    }

    let mut aans = vec![];
    for k in 1..=n {
        aans.push(ans[k].to_string());
    }

    println!("{}", aans.join(" "));
}
