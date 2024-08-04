fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<u128> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn f(aa: &Vec<u128>) -> Vec<usize> {
    let mut rr = vec![0, 0];

    use std::collections::VecDeque;
    let mut queue = VecDeque::from(vec![0]);
    let mut zz = vec![usize::MAX >> 1];

    for i in 1..aa.len() {
        let mut al = aa[i - 1];
        let mut ar = aa[i];

        if al >= ar {
            let mut d = 0;
            while al >= ar * 4 {
                ar *= 4;
                d += 1;
            }
            zz.push(d);
            if d > 0 {
                queue.push_back(i);
            }
            rr.push(*rr.last().unwrap());
        } else {
            let mut d = 0;
            while al < ar {
                al *= 4;
                d += 1;
            }
            zz.push(0);

            let mut r = *rr.last().unwrap();
            while d > 0 {
                let j = queue.pop_back().unwrap();
                let v = std::cmp::min(zz[j], d);
                zz[j] -= v;
                d -= v;
                r += v * (i - j);

                if zz[j] > 0 {
                    queue.push_back(j);
                }
            }
            rr.push(r);
        }
    }

    rr
}

fn main() {
    let n = read_vec()[0] as usize;
    let aa = read_vec();
    let mut aa_r = aa.clone();
    aa_r.reverse();

    let xx_l = f(&aa);
    let xx_r = f(&aa_r);

    let mut ans = usize::MAX;

    for nl in 0..=n {
        let nr = n - nl;
        let a = (xx_l[nl] + xx_r[nr]) * 2 + nl;
        ans = std::cmp::min(ans, a);
    }

    println!("{}", ans);
}
