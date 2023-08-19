use std::collections::BinaryHeap;

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn read_int_vec() -> Vec<usize> {
    input()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect()
}

fn main() {
    let nm = read_int_vec();
    let n = nm[0];
    let m = nm[1];

    let alist = read_int_vec();
    let mut rlist = vec![0; n + 1];

    for _ in 0..m {
        let lr = read_int_vec();
        let l = lr[0];
        let r = lr[1];

        rlist[l] = std::cmp::max(rlist[l], r);
    }

    let mut heap = BinaryHeap::new();
    heap.push((-(n as i64), n + 1));

    let mut dp = vec![0; n + 1];

    for i in 1..=n {
        loop {
            if let Some(&(_, r)) = heap.peek() {
                if r < i {
                    heap.pop();
                } else {
                    break;
                }
            }
        }
        if let Some(&(l, _)) = heap.peek() {
            let l = (-l) as usize;
            // println!("(i,l) = {}, {}", i, l);

            let j = std::cmp::min(i, l) - 1;
            dp[i] = std::cmp::max(dp[i - 1], dp[j] + alist[i - 1]);
        }

        if rlist[i] > 0 {
            heap.push((-(i as i64), rlist[i]));
        }
    }

    // println!("rlist={:?}", rlist);
    // println!("dp={:?}", dp);

    if let Some(ans) = dp.pop() {
        println!("{}", ans);
    }
}
