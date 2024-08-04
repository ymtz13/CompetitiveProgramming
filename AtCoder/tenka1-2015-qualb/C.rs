const MOD: i64 = 1000000007;
const INV2: i64 = 500000004;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn s(v0: i64, d: i64, n: i64) -> i64 {
    let v0 = v0 % MOD;
    let n = n % MOD;

    let mut ret = v0 * n % MOD;
    ret += (d * n * (n + MOD - 1) % MOD) * INV2 % MOD;
    ret % MOD
}

fn solve(l: i64) -> i64 {
    if l < 9 {
        return 0;
    }

    let m = (l + 3) / 4;
    let n1 = m - 2;
    let n2 = (l - 1) / 2 - m;

    let s1 = s(0, 2, n1);
    let s2 = s(l - 2 * (m + 1), -2, n2);

    let t1 = l / 3 - m;
    let t2 = (l + 1) / 3 - m;
    let t3 = (l + 2) / 3 - m;
    // println!("{:?}", (m, (n1, n2), (s1, s2), (t1, t2, t3)));

    ((s1 + s2 - t1 - t2 - t3) % MOD + MOD) % MOD
}

fn main() {
    let l: i64 = read_line().parse().unwrap();

    println!("{}", solve(l));
}
