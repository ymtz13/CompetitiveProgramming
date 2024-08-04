fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let n = read_vec()[0];
    let aa = read_vec();
    let bb = read_vec();

    let mut kkk = vec![];
    for i in 0..n {
        let a = aa[i];
        let b = bb[i];

        if a < b {
            println!("-1");
            return;
        }

        if a == b {
            continue;
        }

        let mut stack = vec![(a, 0u64)];
        let mut kk = vec![];
        while let Some((x, k)) = stack.pop() {
            if x == b {
                kk.push(k);
                continue;
            }

            for q in b + 1..=x {
                let r = x % q;
                if r >= b {
                    stack.push((r, k | (1 << q)));
                }
            }
        }

        if kk.len() == 0 {
            println!("-1");
            return;
        }

        // for &k in &kk {
        //     println!("{:>#30b}", k >> 1);
        // }

        kkk.push(kk);
    }

    let mut ans = 0;

    for i in (1..=50).rev() {
        let v = 1 << i;

        let mut kkkf = vec![];
        let mut ok = true;
        for kk in &kkk {
            let kkf: Vec<_> = kk.iter().cloned().filter(|&k| k & v == 0).collect();

            if kkf.len() == 0 {
                ok = false;
                break;
            }

            kkkf.push(kkf);
        }

        if ok {
            kkk = kkkf;
        } else {
            ans += v;
        }
    }

    println!("{ans}");
}
