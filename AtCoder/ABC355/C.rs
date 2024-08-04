fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let nt = read_vec();
    let n = nt[0];
    let t = nt[1];

    let aa = read_vec();

    let mut cnt_h = vec![0; n];
    let mut cnt_v = vec![0; n];
    let mut cnt_d0 = 0;
    let mut cnt_d1 = 0;

    for i in 1..=t {
        let a = aa[i - 1] - 1;
        let ih = a / n;
        let iv = a % n;

        cnt_h[ih] += 1;
        cnt_v[iv] += 1;

        if ih == iv {
            cnt_d0 += 1;
        }

        if ih + iv == n - 1 {
            cnt_d1 += 1;
        }

        if cnt_h[ih] == n || cnt_v[iv] == n || cnt_d0 == n || cnt_d1 == n {
            println!("{i}");
            return;
        }
    }

    println!("-1");
}
