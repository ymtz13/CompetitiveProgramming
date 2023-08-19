use std::str::FromStr;

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn read_tuple3<T: FromStr, U: FromStr, V: FromStr>() -> Result<(T, U, V), ()> {
    let items = input();
    let mut items = items.split_whitespace();

    let t = items.next().unwrap().parse();
    let u = items.next().unwrap().parse();
    let v = items.next().unwrap().parse();

    if let (Ok(t), Ok(u), Ok(v)) = (t, u, v) {
        return Ok((t, u, v));
    }

    Err(())
}

fn read_vec<T: FromStr>() -> Result<Vec<T>, ()> {
    let items = input();
    let mut result: Vec<T> = Vec::new();

    for item in items.split_whitespace() {
        match item.parse() {
            Ok(v) => result.push(v),
            Err(_) => return Err(()),
        }
    }

    Ok(result)
}

use std::collections::HashMap;

fn f(available: &Vec<usize>) -> i64 {
    available;
    1
}

const M: usize = 5;

fn main() {
    let n: usize = input().trim().parse().unwrap();

    let s = input();
    let s: Vec<_> = s.trim().bytes().map(|c| c - b'A').collect();

    let mut cnt = vec![vec![0; M]; M];
    for (c0, c1) in s.iter().zip(&s[1..]) {
        let c0 = usize::from(*c0);
        let c1 = usize::from(*c1);
        cnt[c0][c1] += if c0 != c1 { 2 } else { 1 };
    }
    println!("{:?}", cnt);

    let c1 = s.first().unwrap();
    let cn = s.last().unwrap();

    let mut xnmap = HashMap::<i64, i64>::new();

    if c1 == cn {
        let available = vec![(1 << M) - 1; M];
        xnmap.insert(0, f(&available));
    } else {
        let b1 = 1 << c1;
        let bn = 1 << cn;

        for x1 in 0..M {
            for xn in 0..M {
                if x1 == xn {
                    continue;
                }

                let mut available = vec![(1 << M) - 1 - b1 - bn; M];
                available[x1] = b1;
                available[xn] = bn;

                println!("{} {} {:?}", x1, xn, available);
            }
        }
    }

    let q: usize = input().trim().parse().unwrap();
    for _ in 0..q {
        let (a, l, r): (usize, usize, usize) = read_tuple3().unwrap();

        println!("{} {} {}", a, l, r);
    }
}

// nL + nR = n
// nL - nR = x

// nL = (n+x)/2
// nR = (n-x)/2

// score = L * nL + R * nR = (L+R)*n/2 + (L-R)*x/2
