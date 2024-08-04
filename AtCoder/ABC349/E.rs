fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_iii() -> (i64, i64, i64) {
    let s = read_line();
    let mut iter = s.split_whitespace().map(|c| c.parse().unwrap());
    (iter.next().unwrap(), iter.next().unwrap(), iter.next().unwrap())
}

fn dfs(aa: &Vec<i64>, ss: &Vec<usize>, turn: usize) -> usize {
    let curr = turn % 2;
    let prev = 1 - curr;

    if false
        || (ss[0] == prev && ss[1] == prev && ss[2] == prev)
        || (ss[3] == prev && ss[4] == prev && ss[5] == prev)
        || (ss[6] == prev && ss[7] == prev && ss[8] == prev)
        || (ss[0] == prev && ss[3] == prev && ss[6] == prev)
        || (ss[1] == prev && ss[4] == prev && ss[7] == prev)
        || (ss[2] == prev && ss[5] == prev && ss[8] == prev)
        || (ss[0] == prev && ss[4] == prev && ss[8] == prev)
        || (ss[2] == prev && ss[4] == prev && ss[6] == prev)
    {
        return prev;
    }

    if turn == 9 {
        let mut p = vec![0, 0];
        for i in 0..9 {
            p[ss[i]] += aa[i];
        }
        return if p[0] > p[1] { 0 } else { 1 };
    }

    for i in 0..9 {
        if ss[i] != 2 {
            continue;
        }
        let mut ss_next = ss.clone();
        ss_next[i] = curr;

        let res = dfs(aa, &ss_next, turn + 1);
        if res == curr {
            return curr;
        }
    }

    return prev;
}

fn main() {
    let mut aa = vec![];
    for _ in 0..3 {
        let a = read_iii();
        aa.push(a.0);
        aa.push(a.1);
        aa.push(a.2);
    }

    let ss = vec![2; 9];
    let ans = dfs(&aa, &ss, 0);
    // println!("{:?}", aa);
    println!("{}", if ans == 0 { "Takahashi" } else { "Aoki" });
}
