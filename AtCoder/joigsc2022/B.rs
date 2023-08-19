use std::i64;

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("");
    input
}

fn bisect(arr: &Vec<i64>, v: i64) -> Vec<i64> {
    let mut ok = 0;
    let mut ng = arr.len();

    while ng - ok > 1 {
        let tgt = (ok + ng) / 2;
        if arr[tgt] <= v {
            ok = tgt
        } else {
            ng = tgt
        }
    }

    //(arr[ok], arr[ok + 1])
    vec![arr[ok], arr[ok + 1]]
}

fn main() {
    let n: usize = input().trim().parse().expect("");

    let mut js = vec![i64::MIN];
    let mut os = vec![i64::MIN];
    let mut is = vec![i64::MIN];
    let mut gs = vec![i64::MIN];

    for _ in 0..n {
        let ac = input();
        let ac: Vec<&str> = ac.split_whitespace().collect();
        let a = ac[0].parse().expect("");
        let c = ac[1].chars().nth(0).unwrap();

        match c {
            'J' => {
                js.push(a);
            }
            'O' => {
                os.push(a);
            }
            'I' => {
                is.push(a);
            }
            'G' => {
                gs.push(a);
            }
            _ => {}
        }
    }

    js.push(i64::MAX);
    os.push(i64::MAX);
    is.push(i64::MAX);
    gs.push(i64::MAX);

    let q: usize = input().trim().parse().expect("");
    for _ in 0..q {
        let st: Vec<i64> = input()
            .split_whitespace()
            .map(|c| c.parse().expect(""))
            .collect();
        let s = st[0];
        let t = st[1];

        let mut ans = i64::MAX;

        for j in bisect(&js, s) {
            if j == i64::MIN || j == i64::MAX {
                continue;
            }

            for o in bisect(&os, j) {
                if o == i64::MIN || o == i64::MAX {
                    continue;
                }

                for i in bisect(&is, o) {
                    if i == i64::MIN || i == i64::MAX {
                        continue;
                    }

                    for g in bisect(&gs, i) {
                        if g == i64::MIN || g == i64::MAX {
                            continue;
                        }

                        let d = (j - s).abs()
                            + (o - j).abs()
                            + (i - o).abs()
                            + (g - i).abs()
                            + (t - g).abs();

                        // println!("{s} {j} {o} {i} {g} {t} : {d}");
                        ans = std::cmp::min(ans, d);
                    }
                }
            }
        }

        println!("{}", ans);
    }
}
