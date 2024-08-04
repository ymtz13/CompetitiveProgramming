fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn solve(aa: &Vec<usize>) -> i64 {
    let a1 = aa[0] as i64;
    let a2 = aa[1] as i64;
    let xor = aa.iter().fold(0, |xor, a| xor ^ a) as i64;

    let m = 20;

    let mask_r = (1 << m) - 1;
    let mask_l = mask_r << m;

    let a1_l = a1 & mask_l;
    let a1_r = a1 & mask_r;
    let a2_l = a2 & mask_l;
    let a2_r = a2 & mask_r;

    let mut map_l = std::collections::HashMap::<i64, Vec<i64>>::new();
    let mut map_r = std::collections::HashMap::<i64, Vec<i64>>::new();

    for x_r in 0..=mask_r {
        let x_l = x_r << m;

        let b1_l = a1_l ^ x_l;
        let b1_r = a1_r ^ x_r;

        let b2_l = (a2_l ^ xor ^ x_l) & mask_l;
        let b2_r = (a2_r ^ xor ^ x_r) & mask_r;

        let d1_l = a1_l - b1_l;
        let d1_r = a1_r - b1_r;
        let d2_l = a2_l - b2_l;
        let d2_r = a2_r - b2_r;

        // println!("x_r:{x_r:0>2b}");

        map_l.entry(d1_l + d2_l).and_modify(|v| v.push(d1_l)).or_insert(vec![d1_l]);
        map_r.entry(d1_r + d2_r).and_modify(|v| v.push(d1_r)).or_insert(vec![d1_r]);
    }

    // println!("{map_l:?}");
    // println!("{map_r:?}");

    for dd_l in map_l.values_mut() {
        dd_l.sort();
    }

    let mut ans = a1;
    for (&s_l, dd_l) in map_l.iter() {
        if let Some(dd_r) = map_r.get(&-s_l) {
            for &d_r in dd_r {
                let mut i = dd_l.len();
                let mut l = 1 << m;
                while l > 0 {
                    if i >= l && dd_l[i - l] + d_r >= 0 {
                        i = i - l;
                    }
                    l >>= 1;
                }

                if i < dd_l.len() {
                    let s = dd_l[i] + d_r;
                    if s < a1 {
                        ans = std::cmp::min(ans, s);
                    }
                }
            }
        }
    }

    if ans != a1 {
        ans
    } else {
        -1
    }
}

fn main() {
    read_line();
    let aa = read_vec();
    let ans = solve(&aa);
    println!("{ans}");
}
