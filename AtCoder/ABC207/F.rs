fn read_line() -> String {
    let mut s = String();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let edges = vec![vec![]; n + 1];
    for _ in 1..n {
        let uv = read_line();
        let uv: Vec<_> = uv.split_whitespace().map(|c| c.parse().unwrap()).collect();
        let u = uv[0];
        let v = uv[1];

        edges[u].push(v);
        edges[v].push(u);
    }
}
