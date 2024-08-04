fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn dfs(memo: &mut Vec<i8>, edges: &Vec<Vec<bool>>, game: usize) -> i8 {
    if memo[game] != -1 {
        // println!("memo: {game}");
        return memo[game];
    }

    let mut p = vec![];
    for i in 0..edges.len() {
        if (game >> i) & 1 == 1 {
            p.push(i);
        }
    }

    let mut v = 0;

    for i in 0..p.len() {
        for j in i + 1..p.len() {
            let pi = p[i];
            let pj = p[j];

            if edges[pi][pj] {
                if dfs(memo, edges, game - (1 << pi) - (1 << pj)) == 0 {
                    v = 1;
                    break;
                }
            }
        }

        if v == 1 {
            break;
        }
    }

    // println!("game:{game} v:{v}");

    memo[game] = v;
    return v;
}

fn main() {
    let n: usize = read_line().parse().unwrap();

    let mut ab = vec![];
    for _ in 0..n {
        let v = read_vec();
        ab.push((v[0], v[1]));
    }

    let mut edges = vec![vec![false; n]; n];
    for i in 0..n {
        for j in i + 1..n {
            let abi = ab[i];
            let abj = ab[j];
            if abi.0 == abj.0 || abi.1 == abj.1 {
                edges[i][j] = true;
                edges[j][i] = true;
            }
        }
    }

    let mut memo = vec![-1; 1 << n];
    let ans = dfs(&mut memo, &edges, (1 << n) - 1);

    println!("{}", if ans == 1 { "Takahashi" } else { "Aoki" });
}
