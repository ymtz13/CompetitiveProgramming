fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_ii() -> (i64, i64) {
    let ii: Vec<_> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    (ii[0], ii[1])
}

fn f(aa: &mut Vec<i64>) -> i64 {
    aa.sort();
    let mut ret = 0;
    let mut s = 0;
    for i in 0..aa.len() {
        let a = aa[i];
        ret += a * (i as i64) - s;
        s += a;
    }
    ret
}

fn main() {
    let n: usize = read_line().parse().unwrap();

    let mut p0 = vec![];
    let mut q0 = vec![];
    let mut p1 = vec![];
    let mut q1 = vec![];

    for _ in 0..n {
        let (x, y) = read_ii();

        if (x + y) & 1 == 0 {
            p0.push((x + y) / 2);
            q0.push((x - y) / 2);
        } else {
            p1.push((x + y + 1) / 2);
            q1.push((x - y + 1) / 2);
        }
    }

    let mut ans = 0;
    ans += f(&mut p0);
    ans += f(&mut q0);
    ans += f(&mut p1);
    ans += f(&mut q1);

    println!("{ans}");
}
