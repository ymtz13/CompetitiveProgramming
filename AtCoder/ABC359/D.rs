const MOD: usize = 998244353;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (usize, usize) {
    let v = read_vec();
    (v[0], v[1])
}

fn main() {
    let (n, k) = read_uu();

    let mut mask = vec![1; 1 << k];
    for i in 0..(1 << k) {
        let mut is_palin = true;
        for j in 0..k {
            if (i >> j) & 1 != (i >> (k - 1 - j)) & 1 {
                is_palin = false;
            }
        }

        if is_palin {
            mask[i] = 0;
        }
    }

    let ss = read_line();
    let ss: Vec<_> = ss.bytes().collect();

    let mut vv = vec![0];
    for i in 0..k {
        let mut vv_nxt = vec![];
        let s = ss[i];
        if s == b'A' {
            for &v in &vv {
                vv_nxt.push(v);
            }
        }
        if s == b'B' {
            for &v in &vv {
                vv_nxt.push(v + (1 << i));
            }
        }
        if s == b'?' {
            for &v in &vv {
                vv_nxt.push(v);
                vv_nxt.push(v + (1 << i));
            }
        }

        vv = vv_nxt;
    }

    let mut dp = vec![0; 1 << k];
    for &v in &vv {
        dp[v] = mask[v];
    }

    for i in k..n {
        let s = ss[i];
        let mut dp_nxt = vec![0; 1 << k];

        for f in 0..(1 << k) {
            if s != b'B' {
                let t = f >> 1;
                dp_nxt[t] += dp[f];
                dp_nxt[t] %= MOD;
            }
            if s != b'A' {
                let t = (f + (1 << k)) >> 1;
                dp_nxt[t] += dp[f];
                dp_nxt[t] %= MOD;
            }
        }

        for t in 0..(1 << k) {
            dp_nxt[t] *= mask[t];
        }

        dp = dp_nxt;
    }

    // println!("{dp:?}");

    let mut ans = 0;
    for &v in &dp {
        ans += v;
        ans %= MOD;
    }

    println!("{ans}");
}
