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

    let aa0: Vec<_> = aa.iter().skip(0).step_by(2).cloned().collect();
    let aa1: Vec<_> = aa.iter().skip(1).step_by(2).cloned().collect();

    let nn = n >> 1;
    let bb0 = ntt(nn, &aa0, inverse);
    let bb1 = ntt(nn, &aa1, inverse);

    let roots = ROOTS[n.ilog2() as usize];
    let r = if inverse { roots.0 } else { roots.1 };

    let ww = (0..nn).scan(1, |w, _| {
        let ret = Some(w.clone());
        *w = *w * r % MOD;
        ret
    });

    let iter = ww.zip(bb1.iter()).map(|(w, b1)| w * b1 % MOD).zip(bb0.iter());
    let r0 = iter.clone().map(|(wb1, b0)| (b0 + wb1) % MOD);
    let r1 = iter.clone().map(|(wb1, b0)| (b0 - wb1) % MOD);

    r0.chain(r1).collect()
}

fn main() {
    let aa = vec![1, 2, 3, 4, 5, 6, 7, 8];
    let bb = ntt(1 << 3, &aa, true);
    let cc = ntt(1 << 3, &bb, false);

    let cc: Vec<_> = cc.iter().map(|v| (v + MOD) % MOD).collect();

    println!("{bb:?}");
    println!("{cc:?}");

    let aa0 = vec![1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0];
    let aa1 = vec![2, 2, 1, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0];

    let bb0 = ntt(1 << 4, &aa0, false);
    let bb1 = ntt(1 << 4, &aa1, false);

    let bb: Vec<_> = (0..1 << 4).map(|i| bb0[i] * bb1[i] % MOD).collect();
    let aa = ntt(1 << 4, &bb, true);

    let aa: Vec<_> = aa.iter().map(|v| ((v + MOD) % MOD) / 16).collect();

    println!("{aa:?}");
}
