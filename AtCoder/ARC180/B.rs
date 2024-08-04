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

    let mut heap = vec![vec![]; n];
    for i in 0..n {
        let p = pp[i];
        for j in i + k..n {
            let q = pp[j];
            if p > q {
                let d = p - q;
                heap[d].push(i * n + j);
            }
        }
    }

    let mut ans = vec![];
    let mut done = vec![false; n * n];
    loop {
        let mut key = 0;
        for d in 1..n {
            while let Some(v) = heap[d].pop() {
                if done[v] {
                    continue;
                }
                let i = v / n;
                let j = v % n;
                let p = pp[j];
                let q = pp[i];

                if p > q || q - p > d {
                    continue;
                }

                key = v;
                break;
            }
            if key != 0 {
                break;
            }
        }
        if key == 0 {
            break;
        }

        let i = key / n;
        let j = key % n;
        let p = pp[j];
        let q = pp[i];

        pp[i] = p;
        pp[j] = q;
        done[key] = true;
        ans.push((i + 1, j + 1));

        for jj in i + k..n {
            let key = i * n + jj;
            let q = pp[jj];
            if !done[key] && p > q {
                let d = p - q;
                heap[d].push(key);
            }
        }

        for ii in 0..=(j - k) {
            let key = ii * n + j;
            let p = pp[ii];
            if !done[key] && p > q {
                let d = p - q;
                heap[d].push(key);
            }
        }
    }

    println!("{}", ans.len());
    for &(i, j) in &ans {
        println!("{i} {j}");
    }
}
