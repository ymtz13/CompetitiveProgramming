fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn solve(n: usize, aa: Vec<usize>, bb: Vec<usize>) -> bool {
    if aa.iter().eq(bb.iter()) {
        return true;
    }

    let neva = aa.iter().filter(|&v| v % 2 == 0).count();
    let nevb = bb.iter().filter(|&v| v % 2 == 0).count();
    // println!("(neva, nevb) = {:?}", (neva, nevb));

    if neva != nevb {
        return false;
    }

    if neva == 0 {
        return false;
    }

    let mut ea = false;
    let mut eb = false;
    for i in 0..n - 2 {
        let ca = aa[i..i + 3].iter().filter(|&v| v % 2 == 1).count();
        let cb = bb[i..i + 3].iter().filter(|&v| v % 2 == 1).count();
        // println!("(i, ca, cb) = {:?}", (i, ca, cb));

        ea = ea || ca == 2;
        eb = eb || cb == 2;
    }

    // println!("(ea, eb) = {:?}", (ea, eb));

    if ea != eb {
        return false;
    }

    if ea {
        let mut aa0: Vec<_> = aa.iter().filter(|&v| v % 2 == 0).collect();
        let mut bb0: Vec<_> = bb.iter().filter(|&v| v % 2 == 0).collect();
        let mut aa1: Vec<_> = aa.iter().filter(|&v| v % 2 == 1).collect();
        let mut bb1: Vec<_> = bb.iter().filter(|&v| v % 2 == 1).collect();
        aa1.sort();
        bb1.sort();

        if aa1.iter().ne(bb1.iter()) {
            return false;
        }

        if aa0.len() >= 3 {
            aa0.sort();
            bb0.sort();
        }

        if aa0.iter().ne(bb0.iter()) {
            return false;
        }

        return true;
    }

    let mut xaa = vec![vec![]];
    let mut xbb = vec![vec![]];

    for i in 0..n {
        let a = aa[i];
        let b = bb[i];

        if (a % 2 == 1 || b % 2 == 1) && a != b {
            return false;
        }

        if a % 2 == 1 {
            xaa.push(vec![]);
            xbb.push(vec![]);
        } else {
            let ia = xaa.len() - 1;
            let ib = xbb.len() - 1;

            xaa[ia].push(a);
            xbb[ib].push(b);
        }
    }

    for (xa, xb) in xaa.iter().zip(xbb.iter()) {
        let mut xa = xa.clone();
        let mut xb = xb.clone();

        if xa.len() >= 3 {
            xa.sort();
            xb.sort();
        }

        if xa.iter().ne(xb.iter()) {
            return false;
        }
    }

    true
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let aa = read_vec();
    let bb = read_vec();

    let ans = solve(n, aa, bb);
    println!("{}", if ans { "Yes" } else { "No" });
}
