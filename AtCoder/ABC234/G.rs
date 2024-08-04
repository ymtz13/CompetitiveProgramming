const MOD: i64 = 998244353;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    read_line();
    let aa = read_vec();

    use std::collections::VecDeque;

    let mut s1 = 0;
    let mut s2 = 0;
    let mut vv1 = VecDeque::from(vec![(i64::MAX, 0)]);
    let mut vv2 = VecDeque::from(vec![(i64::MIN, 0)]);
    let mut x = 1;

    for &a in &aa {
        let mut x1 = x;
        while vv1.back().unwrap().0 <= a {
            let (va, vt) = vv1.pop_back().unwrap();
            x1 += vt;
            x1 %= MOD;
            s1 -= va * vt;
            s1 %= MOD;
        }
        vv1.push_back((a, x1));
        s1 += a * x1;
        s1 %= MOD;

        let mut x2 = x;
        while vv2.back().unwrap().0 >= a {
            let (va, vt) = vv2.pop_back().unwrap();
            x2 += vt;
            x2 %= MOD;
            s2 -= va * vt;
            s2 %= MOD;
        }
        vv2.push_back((a, x2));
        s2 += a * x2;
        s2 %= MOD;

        x = s1 - s2;
        x %= MOD;

        // println!("a:{a} x:{x}");
        // println!("vv1:{vv1:?} s1:{s1}");
        // println!("vv2:{vv2:?} s2:{s2}");
    }

    println!("{}", (x + MOD) % MOD);
}
