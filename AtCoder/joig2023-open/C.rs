use std::convert::TryInto;

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("");
    input
}

fn read_int_vec() -> Vec<i64> {
    input()
        .split_whitespace()
        .map(|c| c.parse().expect(""))
        .collect()
}

fn bisect(a: &[i64], v: i64) -> usize {
    let mut l: i64 = -1;
    let mut r: i64 = a.len().try_into().unwrap();

    while r - l > 1 {
        let tgt = (l + r) / 2;
        let t: usize = tgt.try_into().unwrap();

        if a[t] <= v {
            l = tgt;
        } else {
            r = tgt;
        }
    }

    r.try_into().unwrap()
}

fn main() {
    let nmk = read_int_vec();
    let mut a = read_int_vec();
    let b = read_int_vec();

    a.insert(0, std::i64::MIN >> 2);
    a.push(std::i64::MAX >> 2);

    let k = nmk[2];

    for x in b {
        let i = bisect(&a, x);
        let vl = a[i - 1];
        let vr = a[i];

        let t = [0, k - (x - vl), k - (vr - x)];
        let ans = t.iter().max().unwrap();
        println!("{}", *ans);
    }
}
