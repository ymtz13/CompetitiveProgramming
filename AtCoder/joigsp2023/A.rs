fn main() {
    let (n, q): (isize, isize) = Read::read();

    let mut vlist = vec![(0, 0)];
    for _ in 0..n {
        let (x, h): (isize, isize) = Read::read();
        vlist.push((x, -h));
    }

    vlist.sort();

    let vlist: Vec<_> = vlist.iter().map(|c| (c.0, -c.1)).collect();

    let mut filtered_vlist = Vec::new();
    let mut prev = -1;
    for v in &vlist {
        if v.1 > prev {
            filtered_vlist.push(v);
            prev = v.1;
        }
    }

    // println!("{:?}", vlist);
    // println!("{:?}", filtered_vlist);

    let vlist = filtered_vlist;

    let mut anslist = Vec::new();

    for _ in 0..q {
        let (t,): (isize,) = Read::read();

        let mut ok = 0;
        let mut ng = vlist.len();

        while ng - ok > 1 {
            let tgt = (ng + ok) / 2;
            let (x, h) = vlist[tgt];
            if t >= x + h {
                ok = tgt;
            } else {
                ng = tgt;
            }
        }

        // println!("{} {} {:?}", ok, ng, vlist[ok]);
        let mut ans = vlist[ok].1;
        if ok + 1 < vlist.len() {
            ans = std::cmp::max(ans, t - vlist[ok + 1].0);
        }

        anslist.push(ans);
    }

    for ans in &anslist {
        println!("{}", ans);
    }
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
