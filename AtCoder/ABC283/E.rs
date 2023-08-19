use std::cmp::min;

const INF: usize = 1_000_000_000;

fn main() {
    let (h, w): (usize, usize) = Read::read();
    let mut amat = vec![vec![2; w + 2]; 1];

    for _ in 0..h {
        let mut alist: Vec<_> = input()
            .split_whitespace()
            .map(|c| c.parse().unwrap())
            .collect();
        alist.insert(0, 2);
        alist.push(2);
        amat.push(alist);
    }

    amat.push(vec![2; w + 2]);

    let mut dp00 = 0;
    let mut dp01 = 1;
    let mut dp10 = 0;
    let mut dp11 = 1;

    for ih in 2..amat.len() {
        let r0 = &amat[ih - 2];
        let r1 = &amat[ih - 1];
        let r2 = &amat[ih];

        let f0 = flip(&r0);
        let f1 = flip(&r1);
        let f2 = flip(&r2);

        let mut dp00_next = INF;
        let mut dp01_next = INF;
        let mut dp10_next = INF;
        let mut dp11_next = INF;

        if is_ok(&r0, &r1, &r2) {
            dp00_next = dp00;
        }
        if is_ok(&f0, &r1, &r2) {
            dp00_next = min(dp00_next, dp10);
        }

        if is_ok(&r0, &r1, &f2) {
            dp01_next = dp00 + 1;
        }
        if is_ok(&f0, &r1, &f2) {
            dp01_next = min(dp01_next, dp10 + 1);
        }

        if is_ok(&r0, &f1, &r2) {
            dp10_next = dp01;
        }
        if is_ok(&f0, &f1, &r2) {
            dp10_next = min(dp10_next, dp11);
        }

        if is_ok(&r0, &f1, &f2) {
            dp11_next = dp01 + 1;
        }
        if is_ok(&f0, &f1, &f2) {
            dp11_next = min(dp11_next, dp11 + 1);
        }

        // println!("{ih}: {dp00}, {dp01}, {dp10}, {dp11}");

        dp00 = dp00_next;
        dp01 = dp01_next;
        dp10 = dp10_next;
        dp11 = dp11_next;
    }

    let ans = min(dp00, dp10);

    println!("{:?}", if ans < INF { ans as i32 } else { -1 });
}

fn is_ok(r0: &[usize], r1: &[usize], r2: &[usize]) -> bool {
    for iw in 1..r1.len() - 1 {
        let c = r1[iw];
        if r0[iw] != c && r2[iw] != c && r1[iw - 1] != c && r1[iw + 1] != c {
            return false;
        }
    }
    return true;
}

fn flip(r: &[usize]) -> Vec<usize> {
    r.iter().map(|c| c ^ 1).collect()
}

//=============================================================================

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

trait Read {
    fn read() -> Self;
}

impl<T1> Read for (T1,)
where
    T1: std::str::FromStr,
{
    fn read() -> (T1,) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();

        if let Ok(v1) = v1 {
            return (v1,);
        }

        panic!();
    }
}

impl<T1, T2> Read for (T1, T2)
where
    T1: std::str::FromStr,
    T2: std::str::FromStr,
{
    fn read() -> (T1, T2) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();
        let v2 = s.next().unwrap().parse();

        if let (Ok(v1), Ok(v2)) = (v1, v2) {
            return (v1, v2);
        }

        panic!();
    }
}

impl<T1, T2, T3> Read for (T1, T2, T3)
where
    T1: std::str::FromStr,
    T2: std::str::FromStr,
    T3: std::str::FromStr,
{
    fn read() -> (T1, T2, T3) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();
        let v2 = s.next().unwrap().parse();
        let v3 = s.next().unwrap().parse();

        if let (Ok(v1), Ok(v2), Ok(v3)) = (v1, v2, v3) {
            return (v1, v2, v3);
        }

        panic!();
    }
}

impl<T1, T2, T3, T4> Read for (T1, T2, T3, T4)
where
    T1: std::str::FromStr,
    T2: std::str::FromStr,
    T3: std::str::FromStr,
    T4: std::str::FromStr,
{
    fn read() -> (T1, T2, T3, T4) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();
        let v2 = s.next().unwrap().parse();
        let v3 = s.next().unwrap().parse();
        let v4 = s.next().unwrap().parse();

        if let (Ok(v1), Ok(v2), Ok(v3), Ok(v4)) = (v1, v2, v3, v4) {
            return (v1, v2, v3, v4);
        }

        panic!();
    }
}

impl<T1, T2, T3, T4, T5> Read for (T1, T2, T3, T4, T5)
where
    T1: std::str::FromStr,
    T2: std::str::FromStr,
    T3: std::str::FromStr,
    T4: std::str::FromStr,
    T5: std::str::FromStr,
{
    fn read() -> (T1, T2, T3, T4, T5) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();
        let v2 = s.next().unwrap().parse();
        let v3 = s.next().unwrap().parse();
        let v4 = s.next().unwrap().parse();
        let v5 = s.next().unwrap().parse();

        if let (Ok(v1), Ok(v2), Ok(v3), Ok(v4), Ok(v5)) = (v1, v2, v3, v4, v5) {
            return (v1, v2, v3, v4, v5);
        }

        panic!();
    }
}

impl<T1, T2, T3, T4, T5, T6> Read for (T1, T2, T3, T4, T5, T6)
where
    T1: std::str::FromStr,
    T2: std::str::FromStr,
    T3: std::str::FromStr,
    T4: std::str::FromStr,
    T5: std::str::FromStr,
    T6: std::str::FromStr,
{
    fn read() -> (T1, T2, T3, T4, T5, T6) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();
        let v2 = s.next().unwrap().parse();
        let v3 = s.next().unwrap().parse();
        let v4 = s.next().unwrap().parse();
        let v5 = s.next().unwrap().parse();
        let v6 = s.next().unwrap().parse();

        if let (Ok(v1), Ok(v2), Ok(v3), Ok(v4), Ok(v5), Ok(v6)) = (v1, v2, v3, v4, v5, v6) {
            return (v1, v2, v3, v4, v5, v6);
        }

        panic!();
    }
}
