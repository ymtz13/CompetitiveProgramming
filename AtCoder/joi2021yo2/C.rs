use std::collections::BinaryHeap;

fn f(x: i64, heap0: &BinaryHeap<i64>, n2: i64, d: i64, k: i64) -> bool {
    let mut heap = heap0.clone();
    let mut cnt = vec![0, 0];

    while let Some(q) = heap.pop() {
        let time = q / n2;
        let cp = q % n2;
        let c = cp / 2;
        let p = cp % 2;

        if time < 0 {
            return false;
        }

        // println!("time={}, c={}, p={}", time, c, p);

        if c == 0 {
            cnt[p as usize] += 1;

            let event_remain = x - cnt[p as usize];
            let time_move = d + k * event_remain;
            let time_departure = time - 1 - time_move;

            // if time_departure >= 0 {
            heap.push(time_departure * n2 + cnt[p as usize] * 2 + 1 - p);
            // }
        } else {
            cnt[p as usize] = std::cmp::max(cnt[p as usize], c);
        }

        if cnt[p as usize] >= x {
            return true;
        }
    }
    false
}

fn main() {
    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();

    let ndk: Vec<i64> = inp
        .trim()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect();
    let n = ndk[0];
    let d = ndk[1];
    let k = ndk[2];

    let n2 = n * 2 + 5;
    // let e = n + 1;

    let mut heap = BinaryHeap::new();

    for _ in 0..n {
        let mut inp = String::new();
        std::io::stdin().read_line(&mut inp).unwrap();

        let ps: Vec<i64> = inp
            .trim()
            .split_whitespace()
            .map(|c| c.parse().unwrap())
            .collect();
        let p = ps[0];
        let s = ps[1];
        heap.push((s + 1) * n2 + p - 1);
    }

    // println!("{:?}", ndk);

    // println!("{:?}", f(12, &heap, n2, d, k, e));
    // return;

    let mut ng = n + 1;
    let mut ok = 1;
    while ng - ok > 1 {
        let tgt = (ok + ng) / 2;
        if f(tgt, &heap, n2, d, k) {
            ok = tgt
        } else {
            ng = tgt
        }
    }

    println!("{}", ok);
}
