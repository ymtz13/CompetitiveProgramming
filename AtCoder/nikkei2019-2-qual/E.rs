fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let nk = read_vec();
    let n = nk[0];
    let k = nk[1];

    let kmax = (n + 1) / 2;
    if k > kmax {
        println!("-1");
        return;
    }

    let d = kmax - k;

    let mut ans = vec![];

    if n % 2 == 1 {
        for i in 0..kmax {
            ans.push((kmax + i - d, 4 * kmax - 2 + i - d, 5 * kmax - 2 + 2 * i - d));
        }
        for i in 0..kmax - 1 {
            ans.push((2 * kmax + i - d, 3 * kmax - 1 + i - d, 5 * kmax - 1 + 2 * i - d));
        }
    } else {
        for i in 0..kmax {
            ans.push((kmax + i - d, 4 * kmax + i - d, 5 * kmax + 2 * i - d));
        }
        for i in 0..kmax {
            ans.push((2 * kmax + i - d, 3 * kmax + i - d, 5 * kmax + 1 + 2 * i - d));
        }
    }

    for &(a, b, c) in &ans {
        println!("{a} {b} {c}");
    }
}
