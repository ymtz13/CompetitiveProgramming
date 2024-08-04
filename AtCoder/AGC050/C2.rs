fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_i() -> i64 {
    read_line().parse().unwrap()
}

fn solve(aa: &Vec<i64>, l: usize, r: usize, b: usize, memo: &mut Vec<i64>) -> i64 {
    // println!("{l} {r} {b}");
    let key = (b << 20) + (l << 10) + r;
    if memo[key] != i64::MAX {
        return memo[key];
    }

    let mut s = 0;
    let mut ret = i64::MIN;
    for ll in l..r {
        let rend = if b == 1 { r - 1 } else { r };

        for rr in (ll + 3..=rend).step_by(3) {
            let v1 = solve(aa, ll, rr, 1 - b, memo);
            let v2 = solve(aa, rr, r, b, memo);
            // println!("{s} {v1} {v2}");

            let score = s + v1 + v2;
            ret = std::cmp::max(ret, score);
        }

        if b == 1 {
            s += aa[ll];
        }
    }
    ret = std::cmp::max(ret, s);

    // println!("{:?} -> {ret}", (l, r, b));
    memo[key] = ret;
    return ret;
}

fn main() {
    let n = read_i() as usize;
    let mut aa = vec![];

    for _ in 0..n {
        let a = read_i();
        aa.push(a);
    }

    let mut memo = vec![i64::MAX; 1 << 22];

    let ans = solve(&aa, 0, n, 0, &mut memo);

    println!("{ans}");
}
