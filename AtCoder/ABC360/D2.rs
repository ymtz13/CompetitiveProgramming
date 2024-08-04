fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i128> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let nt = read_vec();
    let n = nt[0] as usize;
    let t = nt[1];

    let ss: Vec<_> = read_line().bytes().collect();
    let xx = read_vec();

    let mut ee = vec![];

    for i in 0..n {
        let x = xx[i] * 2;
        if ss[i] == b'0' {
            ee.push((x, i, 0, false));
            ee.push((x - t * 4 - 1, i, 0, true));
        } else {
            ee.push((x, i, 1, true));
            ee.push((x + t * 4 + 1, i, 1, false));
        }
    }

    ee.sort();

    let mut nl = 0;
    let mut nr = 0;
    let mut ans = vec![0; n];

    for &(_, i, d, start) in &ee {
        if d == 0 {
            if start {
                ans[i] = -nr;
            } else {
                ans[i] += nr;
                nl += 1;
            }
        } else {
            if start {
                ans[i] = -nl;
                nr += 1;
            } else {
                ans[i] += nl;
            }
        }
    }

    println!("{ans:?}");

    let mut t = 0;
    for &a in &ans {
        t += a;
    }

    println!("{}", t / 2);
}
