fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn f(tgt: usize, aa: &Vec<usize>) -> bool {
    let mut bb = std::collections::VecDeque::from(vec![(0, aa[0])]);

    // println!("0 {bb:?}");

    for i in 1..aa.len() {
        let a0 = aa[i - 1];
        let a = aa[i];

        if a0 < a {
            bb.push_back((0, a - a0));
        } else {
            let mut s = 0;
            loop {
                let (v, n) = bb.pop_back().unwrap();
                s += n;

                if a0 - s <= a {
                    if a0 - s < a {
                        bb.push_back((v, a + s - a0));
                    }
                    break;
                }
            }

            let mut s = 0;
            loop {
                let b = bb.pop_back();
                if b.is_none() {
                    return false;
                }

                let (v, n) = b.unwrap();
                if v == tgt - 1 {
                    s += n;
                } else {
                    if n > 1 {
                        bb.push_back((v, n - 1));
                    }
                    bb.push_back((v + 1, 1));
                    break;
                }
            }
            if s > 0 {
                bb.push_back((0, s));
            }
        }

        // println!("{i} {bb:?}");
    }

    true
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let aa: Vec<_> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();

    // f(1, &aa);
    // return ();

    let mut ok = n;
    let mut ng = 0;
    while ok - ng > 1 {
        let tgt = (ok + ng) / 2;
        if f(tgt, &aa) {
            ok = tgt;
        } else {
            ng = tgt;
        }
    }

    println!("{ok}");
}
