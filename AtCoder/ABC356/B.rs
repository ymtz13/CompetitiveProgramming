fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (usize, usize) {
    let v: Vec<_> = read_vec();
    (v[0], v[1])
}

fn main() {
    let (n, m) = read_uu();
    let aa = read_vec();
    let mut bb = vec![0; m];

    for i in 0..n {
        let xx = read_vec();
        for j in 0..m {
            bb[j] += xx[j];
        }
    }

    let mut ok = "Yes";
    for j in 0..m {
        if aa[j] > bb[j] {
            ok = "No";
        }
    }

    println!("{ok}");
}
