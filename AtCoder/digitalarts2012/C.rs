fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let nmk = read_vec();
    let n = nmk[0];
    let m = nmk[1];
    let k = nmk[2];

    let c = 300;

    const T: u8 = 0;
    const F: u8 = 1;
    const U: u8 = 2;

    let mut dd = vec![0; n + 1];
    let mut ee = std::collections::HashSet::new();

    let mut logs = vec![];
    for i in 1..=m {
        let log = read_line();
        let log: Vec<_> = log.split_whitespace().collect();

        if log[0] == "t" {
            let j: usize = log[1].parse().unwrap();
            logs.push((i, T, j, 0));
        }

        if log[0] == "f" {
            let j: usize = log[1].parse().unwrap();
            let k: usize = log[2].parse().unwrap();
            logs.push((i, F, j, k));

            dd[j] += 1;
            dd[k] += 1;

            ee.insert(if j < k { (j, k) } else { (k, j) });
        }

        if log[0] == "u" {
            let j: usize = log[1].parse().unwrap();
            let k: usize = log[2].parse().unwrap();
            logs.push((i, U, j, k));

            ee.remove(&if j < k { (j, k) } else { (k, j) });
        }
    }

    for &(j, k) in ee.iter() {
        let i = logs.len() + 1;
        logs.push((i, U, j, k));
    }

    // println!("{logs:?}");
    // println!("{ee:?}");

    let mut pp = vec![false; n + 1];
    let mut qq = vec![];
    let mut cnts = vec![vec![]; n + 1];
    for i in 1..=n {
        if dd[i] >= c {
            pp[i] = true;
            qq.push(i);
            cnts[i].push(0);
        }
    }

    let mut ans = vec![0; n + 1];
    let mut edges = vec![std::collections::HashMap::new(); n + 1];

    for &(i, t, j, k) in &logs {
        for &q in &qq {
            let last = cnts[q][i - 1];
            cnts[q].push(last);
        }

        if t == T {
            ans[j] += 1;
            if pp[j] {
                cnts[j][i] += 1;
            } else {
                for &k in edges[j].keys() {
                    ans[k] += 1;
                }
            }
        }

        if t == F {
            edges[j].insert(k, i);
            edges[k].insert(j, i);
        }

        if t == U {
            let i0 = edges[j].remove(&k).unwrap();
            edges[k].remove(&j);

            if pp[j] {
                ans[k] += cnts[j][i] - cnts[j][i0];
            }
            if pp[k] {
                ans[j] += cnts[k][i] - cnts[k][i0];
            }
        }
    }

    ans.sort();
    ans.reverse();

    println!("{}", ans[k - 1]);
}
