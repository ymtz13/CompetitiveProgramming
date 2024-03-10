fn main() {
    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();
    let nmq: Vec<usize> = inp
        .trim()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect();
    let n = nmq[0];
    let m = nmq[1];
    let q = nmq[2];

    let n2 = n + 2;
    let m2 = m + 2;
    let nm = n2 * m2;

    let mut s = vec![0; nm as usize];
    let mut tu = vec![0; nm as usize];
    let mut td = vec![0; nm as usize];
    let mut tr = vec![0; nm as usize];
    let mut tl = vec![0; nm as usize];
    let mut r = vec![0; nm as usize];

    for i in 1..=n {
        let mut inp = String::new();
        std::io::stdin().read_line(&mut inp).unwrap();
        let mut inp = inp.trim().chars();
        // println!("{:?}", inp);

        for j in 1..=m {
            let c = inp.next();
            let v = if c == Some('0') { 0 } else { 1 };
            s[(i * m2 + j) as usize] = v;
            // println!("{:?}", (i, j, c, v));
        }
    }

    for i in 1..=n {
        for j in 1..=m {
            let k = i * m2 + j;
            if s[k] == 0 {
                continue;
            }

            let mut v = 4;
            if s[k - m2] == 1 {
                tu[k] = 1;
                v -= 1
            }
            if s[k + m2] == 1 {
                td[k] = 1;
                v -= 1
            }
            if s[k - 1] == 1 {
                tl[k] = 1;
                v -= 1
            }
            if s[k + 1] == 1 {
                tr[k] = 1;
                v -= 1
            }

            r[k] = v;
        }
    }

    for i in 1..=n {
        for j in 1..m2 {
            let k = i * m2 + j;
            s[k] += s[k - 1];
            r[k] += r[k - 1];
        }
    }

    for j in 1..m2 {
        for i in 1..n2 {
            let k = i * m2 + j;
            s[k] += s[k - m2];
            r[k] += r[k - m2];
        }
    }

    for i in 1..=n {
        for j in 1..m2 {
            let k = i * m2 + j;
            tu[k] += tu[k - 1];
            td[k] += td[k - 1];
        }
    }

    for j in 1..=m {
        for i in 1..n2 {
            let k = i * m2 + j;
            tr[k] += tr[k - m2];
            tl[k] += tl[k - m2];
        }
    }

    // for i in 0..n2 {
    //     println!("hello {:?}", &s[i * m2..i * m2 + m2]);
    // }
    // for i in 0..n2 {
    //     println!("hello {:?}", &r[i * m2..i * m2 + m2]);
    // }

    for _ in 0..q {
        let mut inp = String::new();
        std::io::stdin().read_line(&mut inp).unwrap();
        let query: Vec<usize> = inp
            .trim()
            .split_whitespace()
            .map(|c| c.parse().unwrap())
            .collect();
        let x1 = query[0];
        let y1 = query[1];
        let x2 = query[2];
        let y2 = query[3];

        let x0 = x1 - 1;
        let y0 = y1 - 1;

        let zs = s[x2 * m2 + y2] - s[x2 * m2 + y0] - s[x0 * m2 + y2] + s[x0 * m2 + y0];
        let zr = r[x2 * m2 + y2] - r[x2 * m2 + y0] - r[x0 * m2 + y2] + r[x0 * m2 + y0];

        let ztu = tu[x1 * m2 + y2] - tu[x1 * m2 + y0];
        let ztd = td[x2 * m2 + y2] - td[x2 * m2 + y0];
        let ztl = tl[x2 * m2 + y1] - tl[x0 * m2 + y1];
        let ztr = tr[x2 * m2 + y2] - tr[x0 * m2 + y2];

        let e = zr + ztu + ztd + ztr + ztl;
        let ans = e / 2 - zs;

        println!("{}", ans);
    }
}
