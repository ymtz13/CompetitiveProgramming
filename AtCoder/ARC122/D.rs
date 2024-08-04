use std::cmp::min;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn solve(b: usize, aa0: &Vec<usize>, aa1: &Vec<usize>) -> usize {
    if b == 0 {
        return 0;
    }

    if aa0.len() == 0 || aa1.len() == 0 {
        return usize::MAX >> 1;
    }

    let mut aa00 = vec![];
    let mut aa01 = vec![];
    let mut aa10 = vec![];
    let mut aa11 = vec![];

    for &a in aa0 {
        if a & b == 0 {
            aa00.push(a);
        } else {
            aa01.push(a);
        }
    }

    for &a in aa1 {
        if a & b == 0 {
            aa10.push(a);
        } else {
            aa11.push(a);
        }
    }

    let bnxt = b >> 1;

    let c0 = aa00.len() > 0 && aa10.len() > 0;
    let c1 = aa01.len() > 0 && aa11.len() > 0;

    if c0 || c1 {
        return min(solve(bnxt, &aa00, &aa10), solve(bnxt, &aa01, &aa11));
    } else {
        return solve(bnxt, aa0, aa1) + b;
    }
}

fn main() {
    read_vec();
    let aa = read_vec();

    let mut mask = 0;

    for i in (0..32).rev() {
        let mut map = std::collections::HashMap::new();
        for &a in &aa {
            map.entry(a & mask).or_insert(vec![]).push(a);
        }

        let b = 1 << i;

        let mut ans = 0;

        for chunk in map.values() {
            let mut aa0 = vec![];
            let mut aa1 = vec![];
            for &a in chunk {
                if b & a == 0 {
                    aa0.push(a);
                } else {
                    aa1.push(a);
                }
            }

            if aa0.len() % 2 == 1 {
                let v = b + solve(b >> 1, &aa0, &aa1);
                ans = std::cmp::max(ans, v);
            }
        }

        if ans > 0 {
            println!("{}", ans);
            return;
        }

        mask |= b;
    }

    println!("0");
}
