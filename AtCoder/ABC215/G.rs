const MOD: i64 = 998244353;

const ROOTS: [(i64, i64); 24] = [
    (1, 1),                 //  0
    (998244352, 998244352), //  1
    (911660635, 86583718),  //  2
    (372528824, 509520358), //  3
    (929031873, 337190230), //  4
    (452798380, 87557064),  //  5
    (922799308, 609441965), //  6
    (781712469, 135236158), //  7
    (476477967, 304459705), //  8
    (166035806, 685443576), //  9
    (258648936, 381598368), // 10
    (584193783, 335559352), // 11
    (63912897, 129292727),  // 12
    (350007156, 358024708), // 13
    (666702199, 814576206), // 14
    (968855178, 708402881), // 15
    (629671588, 283043518), // 16
    (24514907, 3707709),    // 17
    (996173970, 121392023), // 18
    (363395222, 704923114), // 19
    (565042129, 950391366), // 20
    (733596141, 428961804), // 21
    (267099868, 382752275), // 22
    (15311432, 469870224),  // 23
];

fn ntt(n: usize, aa: &Vec<i64>, inverse: bool) -> Vec<i64> {
    if n == 1 {
        return aa.clone();
    }

    let aa0: Vec<_> = aa.iter().enumerate().filter(|(i, _)| i % 2 == 0).map(|(_, a)| a.clone()).collect();
    let aa1: Vec<_> = aa.iter().enumerate().filter(|(i, _)| i % 2 == 1).map(|(_, a)| a.clone()).collect();

    let nn = n >> 1;
    let bb0 = ntt(nn, &aa0, inverse);
    let bb1 = ntt(nn, &aa1, inverse);

    let roots = ROOTS[n.ilog2() as usize];
    let r = if inverse { roots.0 } else { roots.1 };

    let mut ww = vec![];
    let mut w = 1;
    for _ in 0..nn {
        ww.push(w);
        w *= r;
        w %= MOD;
    }

    let zip: Vec<_> = ww.iter().zip(bb0.iter().zip(bb1.iter())).map(|(w, (b0, b1))| (w, *b0, *b1)).collect();

    let r0: Vec<_> = zip.iter().map(|&(w, b0, b1)| (b0 + w * b1) % MOD).collect();
    let r1: Vec<_> = zip.iter().map(|&(w, b0, b1)| (b0 - w * b1) % MOD).collect();

    vec![r0, r1].concat()
}

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn pow(mut n: i64, mut x: usize) -> i64 {
    let mut r = 1;
    while x > 0 {
        if x & 1 == 1 {
            r *= n;
            r %= MOD;
        }
        n *= n;
        n %= MOD;
        x >>= 1;
    }
    r
}

fn inv(n: i64) -> i64 {
    pow(n, MOD as usize - 2)
}

fn main() {
    let n = read_vec()[0] as usize;
    let cc = read_vec();

    let m = 1 << 17;

    let mut pp = vec![0; m];
    pp[0] = 1;
    for i in 1..=n {
        pp[i] = pp[i - 1] * ((n - i + 1) as i64) % MOD;
    }

    // println!("{:?}", &pp[..=n]);

    let mut cnt = std::collections::HashMap::new();
    for c in &cc {
        *cnt.entry(c).or_insert(0) += 1;
    }

    // println!("{cnt:?}");

    let mut aa = vec![0; n + 1];
    for &x in cnt.values() {
        aa[x] += 1;
    }

    // println!("{aa:?} {}", cnt.len());

    let mut bb = vec![];
    for x in 0..=n {
        bb.push(aa[x] * inv(pp[x]) % MOD);
    }
    bb.reverse();

    bb.extend(vec![0; m - bb.len()].iter());

    // println!("{} {}", bb.len(), pp.len());
    // println!("bb: {:?}", &bb[..=n]);
    // println!("pp: {:?}", &pp[..=n]);

    let fbb = ntt(m, &bb, false);
    let fpp = ntt(m, &pp, false);

    let mut fzz = vec![];
    for i in 0..m {
        fzz.push(fbb[i] * fpp[i] % MOD);
    }

    let zz = ntt(m, &fzz, true);

    let minv = inv(m as i64);

    for k in 1..=n {
        let z = zz[n + k] * minv % MOD;
        let ans = cnt.len() as i64 - inv(pp[k]) * z % MOD;
        let ans = (ans % MOD + MOD) % MOD;

        println!("{ans}");
    }
}
