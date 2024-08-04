fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (usize, usize) {
    let v = read_vec();
    (v[0], v[1])
}

fn main() {
    let (n, m) = read_uu();
    let mut ss = vec![];

    for _ in 0..n {
        let s: Vec<_> = read_line().bytes().collect();
        let mut c = 0;
        for j in 0..m {
            if s[j] == b'o' {
                c += 1 << j;
            }
        }
        ss.push(c);
    }

    let mut ans = n;
    for x in 1..(1 << n) {
        let mut c = 0;
        let mut z = 0;
        for i in 0..n {
            if x & (1 << i) > 0 {
                c |= ss[i];
                z += 1;
            }
        }
        if c == (1 << m) - 1 {
            ans = std::cmp::min(ans, z);
        }
    }

    println!("{ans}");
}
