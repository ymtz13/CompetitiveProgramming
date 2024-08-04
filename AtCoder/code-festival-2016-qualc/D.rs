fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (usize, usize) {
    let v = read_vec();
    (v[0], v[1])
}

fn f(ss1: &Vec<u8>, ss2: &Vec<u8>) -> usize {
    let n = ss1.len();
    let mut vvv = vec![vec![0; n + 1]; n + 1];

    for d in 0..=n {
        let mut c = 0;
        for i in 0..n - d {
            if ss1[i] == ss2[i + d] {
                c += 1;
            }
            vvv[n - 1 - i - d][n - 1 - i] = c;
        }
    }

    for d in 1..=n {
        let mut c = 0;
        for i in 0..n - d {
            if ss1[i + d] == ss2[i] {
                c += 1;
            }
            vvv[n - 1 - i][n - 1 - i - d] = c;
        }
    }

    let mut sss = vec![vec![1_000_000; n + 1]; n + 1];
    sss[0][0] = 0;

    use std::cmp::min;
    for i in 0..=n {
        for j in 0..=n {
            if i > 0 {
                sss[i][j] = sss[i - 1][j] + vvv[i - 1][j];
            }
            if j > 0 {
                sss[i][j] = min(sss[i][j], sss[i][j - 1] + vvv[i][j - 1]);
            }
        }
    }

    sss[n][n]
}

fn main() {
    let (h, w) = read_uu();

    let mut ccc = vec![vec![]; w];
    for _ in 0..h {
        let row: Vec<_> = read_line().bytes().collect();
        for iw in 0..w {
            ccc[iw].push(row[iw]);
        }
    }

    let mut ans = 0;
    for iw in 0..w - 1 {
        ans += f(&ccc[iw], &ccc[iw + 1]);
    }

    println!("{ans}");
}
