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

    let mut heap = std::collections::BinaryHeap::new();
    for i in 0..n {
        let p = pp[i];
        for j in i + k..n {
            let q = pp[j];
            if p > q {
                heap.push((n - (p - q), i, j, p, q));
            }
        }
    }

    let mut ans = vec![];
    let mut done = vec![false; n * n];
    while let Some((_, i, j, p, q)) = heap.pop() {
        let key = i * n + j;
        if pp[i] != p || pp[j] != q || done[key] {
            continue;
        }
        let (p, q) = (q, p);
        pp[i] = p;
        pp[j] = q;
        done[key] = true;
        ans.push((i + 1, j + 1));

        for jj in i + k..n {
            let key = i * n + jj;
            let q = pp[jj];
            if !done[key] && p > q {
                heap.push((n - (p - q), i, jj, p, q));
            }
        }

        for ii in 0..=(j - k) {
            let key = ii * n + j;
            let p = pp[ii];
            if !done[key] && p > q {
                heap.push((n - (p - q), ii, j, p, q));
            }
        }
    }

    println!("{}", ans.len());
    for &(i, j) in &ans {
        println!("{i} {j}");
    }
}
