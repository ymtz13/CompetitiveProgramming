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

fn read_uuu() -> (usize, usize, usize) {
    let v = read_vec();
    (v[0], v[1], v[2])
}

use std::collections::HashSet;

fn dfs(used: usize, set: &mut HashSet<Vec<u8>>, s: &Vec<u8>, t: &mut Vec<u8>, k: usize) -> usize {
    let n = s.len();

    if t.len() == n {
        // println!("{t:?}");
        if set.contains(t) {
            return 0;
        }

        set.insert(t.clone());

        for i in 0..=n - k {
            let mut ng = true;
            for l in 0..k / 2 {
                if t[i + l] != t[i + k - 1 - l] {
                    ng = false;
                }
            }
            if ng {
                return 0;
            }
        }
        return 1;
    }

    let mut r = 0;

    for i in 0..s.len() {
        if used & (1 << i) > 0 {
            continue;
        }

        t.push(s[i]);
        r += dfs(used | (1 << i), set, s, t, k);
        t.pop();
    }

    r
}

fn main() {
    let (n, k) = read_uu();
    let s = read_line().into_bytes();
    let mut t = vec![];
    let mut set = HashSet::new();

    println!("{}", dfs(0, &mut set, &s, &mut t, k));
}
