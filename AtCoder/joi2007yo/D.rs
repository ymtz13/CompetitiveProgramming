fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let m: usize = read_line().parse().unwrap();

    let mut aa: Vec<usize> = (1..=2 * n).collect();

    for _ in 0..m {
        let k: usize = read_line().parse().unwrap();
        let mut aanxt = vec![0; 2 * n];

        if k == 0 {
            for i in 0..n {
                aanxt[i * 2] = aa[i];
                aanxt[i * 2 + 1] = aa[i + n];
            }
        } else {
            for i in 0..k {
                aanxt[2 * n - k + i] = aa[i];
            }
            for i in 0..2 * n - k {
                aanxt[i] = aa[i + k];
            }
        }

        aa = aanxt;
    }

    for &a in &aa {
        println!("{a}");
    }
}
