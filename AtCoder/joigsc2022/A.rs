use std::usize;

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("");
    input
}

fn read_int_vec() -> Vec<usize> {
    input()
        .split_whitespace()
        .map(|c| c.parse().expect(""))
        .collect()
}

fn main() {
    let n: usize = input().trim().parse().expect("");
    let mut ab: Vec<(usize, usize)> = Vec::new();
    let mut vl: Vec<(usize, usize)> = Vec::new();
    let mut vr: Vec<(usize, usize)> = Vec::new();

    for _ in 0..n {
        let v = read_int_vec();
        ab.push((v[0], v[1]));
    }

    ab.sort_by_key(|x| x.1);

    let mut xl = (usize::MAX / 2, usize::MAX / 2);
    let mut xr = (usize::MAX / 2, usize::MAX / 2);

    for (a, _) in ab.iter() {
        vl.push(xl.clone());
        let a = *a;

        if a <= xl.0 {
            xl.1 = xl.0;
            xl.0 = a;
        } else if a <= xl.1 {
            xl.1 = a;
        }

        // println!("{xl:?}");
    }

    for (a, b) in ab.iter().rev() {
        vr.push(xr.clone());
        let a = *a + *b;

        if a <= xr.0 {
            xr.1 = xr.0;
            xr.0 = a;
        } else if a <= xr.1 {
            xr.1 = a;
        }

        // println!("{xr:?}");
    }

    vr.reverse();

    // println!("{ab:?}");
    // println!("{vl:?}");
    // println!("{vr:?}");

    let mut ans = usize::MAX;

    for ((a, b), (vl, vr)) in ab.iter().zip(vl.iter().zip(vr.iter())) {
        let mut x = vec![b + vl.0, b + vl.1, vr.0, vr.1];
        x.sort();
        // println!("{a} {b} {vl:?} {vr:?} {x:?}");

        ans = std::cmp::min(ans, a + x[0] + x[1]);
    }

    println!("{}", ans);
}
