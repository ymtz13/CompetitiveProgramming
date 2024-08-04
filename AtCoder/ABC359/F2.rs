fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i128> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let aa = read_vec();

    let mut ok = i128::MAX >> 1;
    let mut ng = 0;
    while ok - ng > 1 {
        let tgt = (ok + ng) / 2;

        let mut esum = 0;
        let mut bk = false;
        for i in 0..n {
            let a = aa[i];
            let e = (tgt / a - 3) / 2;
            if e < 0 {
                bk = true;
                break;
            }
            esum += e;
        }
        if bk {
            ng = tgt;
            continue;
        }

        if esum >= (n - 2) as i128 {
            ok = tgt;
        } else {
            ng = tgt;
        }
    }

    let mut esum = (n - 2) as i128;
    let mut ans = 0;
    for i in 0..n {
        let a = aa[i];
        let e = std::cmp::max(0, std::cmp::min(esum, (ok / a - 3) / 2));
        esum -= e;
        // println!("{a}: {e}");
        ans += (1 + e) * (1 + e) * a;
    }

    // println!("{ok}");
    println!("{ans}");
}
