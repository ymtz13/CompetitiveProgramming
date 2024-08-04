static NULL: usize = 200;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn solve(aa: Vec<(usize, usize)>) -> bool {
    let mut memo = vec![vec![NULL; 105]; 105];
    let g = grundy(&mut memo, &aa, 0, 100);
    g > 0
}

fn grundy(memo: &mut Vec<Vec<usize>>, aa: &Vec<(usize, usize)>, l: usize, r: usize) -> usize {
    if memo[l][r] != NULL {
        return memo[l][r];
    }

    if r <= l {
        memo[l][r] = 0;
        return 0;
    }

    let mut gg = vec![];
    for &(al, ar) in aa.iter().filter(|&(al, ar)| l <= *al && *ar <= r) {
        let gl = grundy(memo, aa, l, al);
        let gr = grundy(memo, aa, ar, r);
        gg.push(gl ^ gr);
    }
    gg.sort();

    let mut mex = 0;
    for &g in gg.iter() {
        if mex == g {
            mex += 1;
        }
    }

    memo[l][r] = mex;
    mex
}

fn main() {
    let t = read_line().parse().unwrap();
    let mut aans = vec![];

    for _ in 0..t {
        let n = read_line().parse().unwrap();
        let mut aa = vec![];
        for _ in 0..n {
            let lr = read_vec();
            aa.push((lr[0], lr[1]));
        }
        let ans = solve(aa);
        aans.push(ans);
    }

    for &ans in aans.iter() {
        println!("{}", if ans { "Alice" } else { "Bob" });
    }
}
