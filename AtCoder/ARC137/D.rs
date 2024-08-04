fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn dfs(i: usize, l: usize, aa: &Vec<usize>) -> Vec<usize> {
    if l == 1 {
        return vec![aa[i]];
    }

    let v0 = dfs(i, l / 2, aa);
    let v1 = dfs(i + l / 2, l / 2, aa);

    let mut vv = v0.clone();
    for i in 0..l / 2 {
        vv[i] ^= v1[i];
    }

    vv.extend(v0);

    vv
}

fn main() {
    let nm = read_vec();
    let n = nm[0];
    let m = nm[1];

    let mut aa = read_vec();
    aa.reverse();

    let mut k = 1;
    while k < n || k < m {
        k *= 2;
    }

    for _ in 0..k - n {
        aa.push(0);
    }

    let ans = dfs(0, k, &aa);

    println!("{}", ans[..m].iter().map(|c| c.to_string()).collect::<Vec<_>>().join(" "));
}

// 0 ooo______
// 1 oo_1_____
// 2 oo__2____
// 3 oo___3___
// 2 o_o1_____
// 3 _oo1_____
// 1 o_o_2____
// 1 _oo_2____
// 0 o__12____
// 3 o__1_3___
// 4 o___23___
