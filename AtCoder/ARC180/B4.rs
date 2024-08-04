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
    let n3 = n * n2;
    let n4 = n * n3;

    let mut heap = std::collections::BinaryHeap::new();
    for i in 0..n {
        let p = pp[i];
        for j in i + k..n {
            let q = pp[j];
            if p > q {
                let d = n - (p - q);
                heap.push(d * n4 + i * n3 + j * n2);
            }
        }
    }

    let mut tt = vec![0; n + 1];
    let mut ans = vec![];
    let mut done = vec![false; n * n];
    while let Some(v) = heap.pop() {
        let ijt = v % n4;
        let i = ijt / n3;
        let jt = ijt % n3;
        let j = jt / n2;
        let t = jt % n2;

        let key = i * n + j;
        if tt[i] > t || tt[j] > t || done[key] {
            continue;
        }
        let p = pp[j];
        let q = pp[i];
        pp[i] = p;
        pp[j] = q;
        done[key] = true;
        ans.push((i + 1, j + 1));

        let tx = ans.len();
        tt[i] = tx;
        tt[j] = tx;

        for jj in i + k..n {
            let key = i * n + jj;
            let q = pp[jj];
            if !done[key] && p > q {
                let d = n - (p - q);
                heap.push(d * n4 + i * n3 + jj * n2 + tx);
            }
        }

        for ii in 0..=(j - k) {
            let key = ii * n + j;
            let p = pp[ii];
            if !done[key] && p > q {
                let d = n - (p - q);
                heap.push(d * n4 + ii * n3 + j * n2 + tx);
            }
        }
    }

    println!("{}", ans.len());
    for &(i, j) in &ans {
        println!("{i} {j}");
    }
}
