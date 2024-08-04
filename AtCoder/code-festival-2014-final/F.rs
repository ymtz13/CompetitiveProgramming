fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn gcd(a: usize, b: usize) -> usize {
    let mut a = a;
    let mut b = b;
    while a > 0 {
        (a, b) = (b % a, a)
    }
    return b;
}

fn main() {
    let n: usize = read_line().parse().unwrap();

    let mut bb = vec![];
    for _ in 0..n {
        let b: usize = read_line().parse().unwrap();
        bb.push(b);
    }

    let mut xx = vec![false; n];
    let mut i0 = n + 1;

    for i in 1..=n {
        let l = i - 1;
        let i = i % n;
        let r = (i + 1) % n;

        let g = gcd(bb[l], bb[r]);
        xx[i] = bb[i] % g != 0;

        if xx[i] {
            i0 = i;
        }
    }

    if i0 == n + 1 {
        println!("0");
    } else {
        let mut ans = n;
        for &st in &vec![i0, (i0 + n - 1) % n, (i0 + n - 2) % n] {
            let mut yy = vec![false; n];
            yy[st] = true;
            yy[(st + 1) % n] = true;
            yy[(st + 2) % n] = true;

            let mut cnt = 1;

            for i in 0..n {
                let i = (st + i) % n;
                if xx[i] && !yy[i] {
                    cnt += 1;
                    yy[i] = true;
                    yy[(i + 1) % n] = true;
                    yy[(i + 2) % n] = true;
                }
            }

            if ans > cnt {
                ans = cnt;
            }
        }

        println!("{}", ans);
    }
}
