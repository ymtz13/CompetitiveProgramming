use std::cmp::{max, min};

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let ss = vec![read_line().into_bytes(), read_line().into_bytes(), read_line().into_bytes()];

    let mut ans = usize::MAX;

    for &(ia, ib, ic) in &vec![(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)] {
        let aa = &ss[ia];
        let bb = &ss[ib];
        let cc = &ss[ic];

        let na = aa.len();
        let nb = bb.len();
        let nc = cc.len();

        let mut dab = vec![];
        let mut dac = vec![];
        let mut dbc = vec![];

        for d in 0..=na {
            let mut ok = true;
            for i in 0..min(na - d, nb) {
                let x = aa[d + i];
                let y = bb[i];
                if x != b'?' && y != b'?' && x != y {
                    ok = false;
                    break;
                }
            }
            if ok {
                dab.push(d);
            }
        }

        for d in 0..=na {
            let mut ok = true;
            for i in 0..min(na - d, nc) {
                let x = aa[d + i];
                let y = cc[i];
                if x != b'?' && y != b'?' && x != y {
                    ok = false;
                    break;
                }
            }
            if ok {
                dac.push(d);
            }
        }

        for d in 0..=nb {
            let mut ok = true;
            for i in 0..min(nb - d, nc) {
                let x = bb[d + i];
                let y = cc[i];
                if x != b'?' && y != b'?' && x != y {
                    ok = false;
                    break;
                }
            }
            if ok {
                dbc.push(d);
            }
        }
        for d in nb + 1..=na {
            dbc.push(d);
        }

        // println!("{:?}", (ia, ib, ic));
        // println!("dab:{dab:?}");
        // println!("dac:{dac:?}");
        // println!("dbc:{dbc:?}");

        let dac: std::collections::HashSet<usize> = dac.iter().cloned().collect();

        for &d1 in &dab {
            for &d2 in &dbc {
                let dd = d1 + d2;
                if dd > na || dac.contains(&dd) {
                    ans = min(ans, max(max(na, d1 + nb), dd + nc));
                }
            }
        }
    }

    println!("{ans}");
}
