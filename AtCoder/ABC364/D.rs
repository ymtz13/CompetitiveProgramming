fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

type Int = i64;

fn read_vec() -> Vec<Int> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_ii() -> (Int, Int) {
    let v = read_vec();
    (v[0], v[1])
}

fn read_iii() -> (Int, Int, Int) {
    let v = read_vec();
    (v[0], v[1], v[2])
}

fn main() {
    let (_, q) = read_ii();
    let mut aa = read_vec();
    aa.push(i64::MIN);
    aa.push(i64::MAX);
    aa.sort();

    let bk: Vec<_> = (0..q).map(|_| read_ii()).collect();

    for &(b, k) in &bk {
        let mut ok = 1 << 30;
        let mut ng = -1;

        while ok - ng > 1 {
            let tgt = (ok + ng) / 2;

            let mut i = 0;
            let mut l = 1 << 20;
            while l > 0 {
                if i + l < aa.len() && aa[i + l] < b - tgt {
                    i += l;
                }
                l >>= 1;
            }

            let mut j = aa.len() - 1;
            let mut l = 1 << 20;
            while l > 0 {
                if l <= j && aa[j - l] > b + tgt {
                    j -= l;
                }
                l >>= 1;
            }

            let cnt = j - i - 1;
            if cnt >= k as usize {
                ok = tgt;
            } else {
                ng = tgt;
            }
        }

        println!("{ok}");
    }
}
