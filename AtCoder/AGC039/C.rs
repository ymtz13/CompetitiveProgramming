const MOD: usize = 998244353;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn pow(mut n: usize, mut k: usize) -> usize {
    let mut r = 1;

    while k > 0 {
        if k & 1 == 1 {
            r *= n;
            r %= MOD;
        }
        n *= n;
        n %= MOD;
        k >>= 1;
    }
    r
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let x = read_line();
    let mut x: Vec<_> = x.bytes().into_iter().map(|c| (c - b'0') as usize).collect();

    let mut total = 1;
    let mut d = 1;
    for &y in x.iter().rev() {
        total += (y as usize) * d % MOD;
        total %= MOD;
        d <<= 1;
        d %= MOD;
    }

    let mut all = true;
    for i in (0..n).rev() {
        if x[i] == 0 {
            x[i] = 1;
            all = false;
            break;
        } else {
            x[i] = 0;
        }
    }

    // println!("{x:?} {all} total:{total}");
    if all {
        x = vec![1; n];
    }

    let none = MOD + 1;
    let mut cc = vec![none; n + 1];
    cc[n] = total;

    for m in 3..=n {
        if m % 2 == 0 || n % m != 0 {
            continue;
        }

        let l = n / m;
        // println!("{l}");

        cc[l] = 0;

        let mut c = 0;
        for i in 0..n {
            let flip = (i / l) % 2;

            if i < l {
                let k = l - i - 1;
                if x[i] == 1 {
                    c += pow(2, k);
                    c %= MOD;
                }
            } else {
                if x[i] == 1 {
                    if x[i % l] == flip {
                        // println!("{l} {i} {c}");
                        c += 1;
                        c %= MOD;
                    }
                }
                if x[i] != x[i % l] ^ flip {
                    // println!("{l} {i} {c}");
                    break;
                }
            }
        }

        cc[l] = c;
    }

    // println!("cc:{:?}", cc.clone());

    let mut ans = 0;

    for i in 1..=n {
        if cc[i] == none {
            continue;
        }
        ans += cc[i] * i * 2;
        ans %= MOD;

        let mut j = i * 2;
        while j <= n {
            if cc[j] != none {
                cc[j] += MOD - cc[i];
                cc[j] %= MOD;
            }
            j += i;
        }
    }

    // println!("cc:{:?}", cc.clone());
    println!("{ans}");

    // let mut ll = vec![];
    // for l in 1..=n {
    //     if n % l != 0 || (n / l) % 2 == 0 {
    //         continue;
    //     }
    //     ll.push(l);
    // } // 2^7 + 2^6+2^5+2^2+2^1 = 128+64+32+4+2 = 230

    // let mut naive = vec![0; n + 1];
    // for z in 0..total {
    //     for &l in &ll {
    //         let mask = (1 << l) - 1;
    //         let pattern = z & mask;

    //         let mut ok = true;
    //         for d in 0..n / l {
    //             let cmp = (z >> (l * d)) & mask;
    //             if d % 2 == 0 {
    //                 if cmp != pattern {
    //                     ok = false;
    //                     break;
    //                 }
    //             } else {
    //                 if mask - cmp != pattern {
    //                     ok = false;
    //                     break;
    //                 }
    //             }
    //         }

    //         if ok {
    //             naive[l] += 1;
    //             break;
    //         }
    //     }
    // }

    // println!("{naive:?}");
}
