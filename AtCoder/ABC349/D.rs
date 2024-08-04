fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_uu() -> (usize, usize) {
    let s = read_line();
    let mut iter = s.split_whitespace().map(|c| c.parse().unwrap());
    (iter.next().unwrap(), iter.next().unwrap())
}

fn dfs(l: usize, r: usize, ans: &mut Vec<(usize, usize)>) {
    if l >= r {
        return;
    }

    for x in (0..=61).rev() {
        let b = 1 << x;

        let jl = (l + b - 1) / b;
        let jr = r / b;
        if jl < jr {
            for i in jl + 1..=jr {
                let ll = (i - 1) * b;
                let rr = i * b;
                ans.push((ll, rr));
            }
            dfs(l, jl * b, ans);
            dfs(jr * b, r, ans);

            break;
        }
    }
}

fn main() {
    let (l, r) = read_uu();

    let mut ans = vec![];
    dfs(l, r, &mut ans);

    ans.sort();

    println!("{}", ans.len());
    for &(l, r) in &ans {
        println!("{} {}", l, r);
    }
}
