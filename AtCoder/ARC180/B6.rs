fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let nk = read_vec();
    let n = nk[0];
    let k = nk[1];
    let mut pp = read_vec();

    let n2 = n * n;

    let mut heap = std::collections::BinaryHeap::new();
    for i in 0..n {
        let p = pp[i];
        for j in i + k..n {
            let q = pp[j];
            if p > q {
                let d = n - (p - q);
                heap.push(d * n2 + i * n + j);
            }
        }
    }

    let mut ans = vec![];
    let mut done = vec![false; n * n];
    while let Some(v) = heap.pop() {
        let key = v % n2;
        if done[key] {
            continue;
        }

        let d = n - v / n2;
        let i = key / n;
        let j = key % n;

        let p = pp[j];
        let q = pp[i];

        println!(
            "{:?} {:?}",
            heap.clone()
                .into_sorted_vec()
                .iter()
                .map(|v| {
                    let key = v % n2;
                    let d = n - v / n2;
                    let i = key / n;
                    let j = key % n;
                    (d, i + 1, j + 1)
                })
                .collect::<Vec<_>>(),
            (d, i + 1, j + 1)
        );

        if p > q || q - p > d {
            continue;
        }
        pp[i] = p;
        pp[j] = q;
        done[key] = true;
        ans.push((i + 1, j + 1));

        for jj in i + k..n {
            let key = i * n + jj;
            let q = pp[jj];
            if !done[key] && p > q {
                let d = n - (p - q);
                heap.push(d * n2 + key);
            }
        }

        for ii in 0..=(j - k) {
            let key = ii * n + j;
            let p = pp[ii];
            if !done[key] && p > q {
                let d = n - (p - q);
                heap.push(d * n2 + key);
            }
        }
    }

    println!("{}", ans.len());
    for &(i, j) in &ans {
        println!("{i} {j}");
    }
}
