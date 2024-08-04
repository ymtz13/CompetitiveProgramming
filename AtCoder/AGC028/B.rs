const MOD: i64 = 1_000_000_007;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn pow(x: i64, p: i64) -> i64 {
    let mut ret = 1;
    let mut x = x;
    let mut p = p;

    while p > 0 {
        if p & 1 == 1 {
            ret *= x;
            ret %= MOD;
        }

        x *= x;
        x %= MOD;

        p >>= 1;
    }

    ret
}

fn inv(x: i64) -> i64 {
    pow(x, MOD - 2)
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let aa: Vec<i64> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();

    let s = aa.iter().sum::<i64>() % (MOD as i64);
    let mut tl = vec![0];
    let mut tr = vec![0];
    let mut sl = 0;
    let mut sr = 0;
    for i in 0..n {
        sl += aa[i];
        sr += aa[n - 1 - i];
        tl.push((tl[tl.len() - 1] + sl) % MOD);
        tr.push((tr[tr.len() - 1] + sr) % MOD);
    }

    let mut ss = vec![0; n + 1];
    for i in 1..=n {
        let ii = i as i64;
        ss[i] = s * ii % MOD - tl[i - 1] - tr[i - 1];
        ss[i] %= MOD;
    }

    let mut f = vec![1];
    for i in 1..=n {
        let ii = i as i64;
        f.push(f[i - 1] * ii % MOD);
    }

    let mut ans = s * f[n] % MOD;

    let mut sl = 0;
    let mut sr = 0;

    for k in 1..n {
        sl += aa[k - 1];
        sr += aa[n - k];
        sl %= MOD;
        sr %= MOD;

        let s1 = (sl + sr) % MOD;
        let s2 = (ss[k] - s1) % MOD;

        let kk = k as i64;

        let mut x1 = f[n];
        x1 = x1 * inv(kk + 1) % MOD;

        ans += s1 * x1 % MOD;
        ans %= MOD;

        if k + 2 <= n {
            let mut x2 = f[n] * 2;
            x2 = x2 * inv(kk + 2) % MOD;
            x2 = x2 * inv(kk + 1) % MOD;

            ans += s2 * x2 % MOD;
            ans %= MOD;
        }
    }

    if ans < 0 {
        ans += MOD;
    }

    println!("{ans}");
}
