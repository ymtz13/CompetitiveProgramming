const INF: usize = usize::MAX >> 1;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_uuu() -> (usize, usize, usize) {
    let a: Vec<_> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    (a[0], a[1], a[2])
}

fn solve(n: usize, tx: Vec<(usize, usize)>) -> usize {
    let mut xxx = vec![vec![]; 100001];
    for &(t, x) in &tx {
        xxx[t].push(x);
    }

    for xx in xxx.iter_mut() {
        xx.sort();
    }

    xxx.reverse();

    let xxx: Vec<_> = xxx.into_iter().filter(|xx| xx.len() > 0).collect();

    // println!("{xxx:?}");

    let mut dp = vec![0; n + 2];
    dp[0] = INF;
    dp[n + 1] = INF;

    for xx in &xxx {
        let mut chunks = vec![];
        let mut s = INF;
        let mut prev = INF;

        for &x in xx {
            if prev + 1 != x {
                if prev != INF {
                    chunks.push((s - 1, prev + 1));
                }
                s = x;
            }
            prev = x;
        }
        chunks.push((s - 1, prev + 1));

        // println!("{chunks:?}");

        for &(l, r) in &chunks {
            for i in l + 1..r {
                dp[i] = std::cmp::min(dp[l] + i - l, dp[r] + r - i);
            }
        }

        // println!("{:?}", dp);
    }

    *dp.iter().min().unwrap()
}

fn main() {
    let (w, h, q) = read_uuu();

    let mut txw = vec![];
    let mut txh = vec![];

    for _ in 0..q {
        let (t, d, x) = read_uuu();

        if d == 0 {
            txw.push((t, x));
        } else {
            txh.push((t, x));
        }
    }

    let ans = solve(w, txw) + solve(h, txh);
    println!("{}", if ans < INF { ans as i64 } else { -1 });
}
