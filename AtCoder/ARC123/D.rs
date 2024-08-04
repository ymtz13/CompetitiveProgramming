use std::io::stdin;

fn main() {
    let mut s = String::with_capacity(10);
    stdin().read_line(&mut s).unwrap();

    let mut s = String::with_capacity(2_400_000);
    stdin().read_line(&mut s).unwrap();

    let aa: Vec<i64> = s.split_whitespace().map(|c| c.parse().unwrap()).collect();
    let n = aa.len();

    let mut inc = aa[0];
    let mut dec = 0;
    let mut bb = vec![inc, dec];

    for i in 1..n {
        let d = aa[i] - aa[i - 1];
        if d > 0 {
            inc += d;
        } else {
            dec -= d;
        }
        bb.push(inc);
        bb.push(dec);
    }
    bb.sort();

    let ans0: i64 = bb[..n].iter().sum();
    let ans1: i64 = bb[n..].iter().sum();
    let ans = ans1 - ans0;

    println!("{ans}");
}
