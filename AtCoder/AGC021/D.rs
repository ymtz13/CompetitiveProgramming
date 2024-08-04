fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn solve(s: &Vec<u8>, k: usize, l: usize, r: usize, memo: &mut Vec<usize>) -> usize {
    if r < l {
        return 0;
    }
    if r == l {
        return 1;
    }

    let len = s.len();
    let key = k * len * len + l * len + r;
    if memo[key] != usize::MAX {
        return memo[key];
    }

    let ret;
    if s[l] == s[r] {
        ret = solve(s, k, l + 1, r - 1, memo) + 2;
    } else {
        let r1 = solve(s, k, l + 1, r, memo);
        let r2 = solve(s, k, l, r - 1, memo);
        let r3 = if k == 0 { 0 } else { solve(s, k - 1, l + 1, r - 1, memo) + 2 };

        ret = *vec![r1, r2, r3].iter().max().unwrap();
    }

    memo[key] = ret;
    ret
}

fn main() {
    let s: Vec<_> = read_line().bytes().collect();
    let k: usize = read_line().parse().unwrap();

    let mut memo = vec![usize::MAX; 30_000_000];
    let ans = solve(&s, k, 0, s.len() - 1, &mut memo);
    println!("{ans}");
}
