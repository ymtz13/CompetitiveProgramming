fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> (Vec<usize>, bool) {
    let vv = read_line();
    let vv: Vec<_> = vv.split_whitespace().collect();

    let mut aa: Vec<usize> = vec![];
    for i in 1..vv.len() - 1 {
        aa.push(vv[i].parse().unwrap());
    }

    (aa, vv[vv.len() - 1] == "o")
}

fn read_uuu() -> (usize, usize, usize) {
    let v: Vec<_> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    (v[0], v[1], v[2])
}

fn main() {
    let (n, m, k) = read_uuu();
    let mut cc = vec![];
    for _ in 0..m {
        cc.push(read_vec());
    }

    let mut ans = 0;
    for bvec in 0..(1 << n) {
        let mut ok = true;
        for (aa, r) in &cc {
            let mut cnt = 0;
            for a in aa {
                if (bvec & (1 << (a - 1))) > 0 {
                    cnt += 1;
                }
            }
            if (cnt >= k && !r) || (cnt < k && *r) {
                ok = false;
                break;
            }
        }

        if ok {
            ans += 1;
        }
    }

    println!("{ans}");
}
