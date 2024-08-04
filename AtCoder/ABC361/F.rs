fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let n: i128 = read_line().parse().unwrap();
    if n <= 3 {
        println!("1");
        return;
    }

    let mut ng = 1_000_000_001;
    let mut ok = 1;
    while ng - ok > 1 {
        let tgt = (ng + ok) / 2;
        if tgt * tgt > n {
            ng = tgt
        } else {
            ok = tgt;
        }
    }

    let mut set = std::collections::HashSet::new();
    let mut cnt = 0;

    for a in 2..n {
        let mut x = a * a * a;
        if x > n {
            break;
        }

        let mut is_sq = false;
        for c in 2..a {
            if c * c == a {
                is_sq = true;
            }
            if c * c >= a {
                break;
            }
        }

        for b in 3..100 {
            if x > n {
                break;
            }
            if !set.contains(&x) {
                set.insert(x);
                if b % 2 == 0 || is_sq {
                    cnt += 1;
                }
            }

            x *= a;
        }
    }

    // println!("{set:?} {cnt}");

    let ans = ok + set.len() as i128 - cnt;

    println!("{ans}");
}
