fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uuu() -> (usize, usize, usize) {
    let v = read_vec();
    (v[0], v[1], v[2])
}

fn main() {
    let n = read_vec()[0];
    let mut ss: Vec<_> = read_line().bytes().collect();
    let mut tt: Vec<_> = read_line().bytes().collect();

    let mut s = 0;
    let mut t = 0;
    for i in 0..n {
        if ss[i] == b'B' {
            s += 1 << i;
        }
        if tt[i] == b'B' {
            t += 1 << i;
        }
    }

    let n2 = n + 2;

    let mut dist = vec![usize::MAX; (n + 1) << n2];
    let mut queue = std::collections::VecDeque::new();
    queue.push_back((s, n, 0));

    while let Some((x, z, d)) = queue.pop_front() {
        if dist[(z << n2) | x] != usize::MAX {
            continue;
        }
        dist[(z << n2) | x] = d;

        for w in 0..=n {
            let diff = if z > w { z - w } else { w - z };
            if diff <= 1 {
                continue;
            }

            let w0 = (x >> w) & 1;
            let w1 = (x >> (w + 1)) & 1;

            let xx = x - (w0 << w) - (w1 << (w + 1));
            let xx = xx + (w0 << z) + (w1 << (z + 1));

            queue.push_back((xx, w, d + 1));
        }
    }

    let ans = dist[(n << n2) | t];
    println!("{}", if ans < usize::MAX { ans as i64 } else { -1 });
}
