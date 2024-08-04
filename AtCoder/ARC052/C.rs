fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

type Int = usize;

fn read_vec() -> Vec<Int> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_ii() -> (Int, Int) {
    let v = read_vec();
    (v[0], v[1])
}

fn read_iii() -> (Int, Int, Int) {
    let v = read_vec();
    (v[0], v[1], v[2])
}

fn main() {
    let (n, m) = read_ii();
    let mut edges = vec![vec![]; n];
    for _ in 0..m {
        let (c, a, b) = read_iii();
        edges[a].push((b, c));
        edges[b].push((a, c));
    }

    let mut dist = vec![i64::MAX; n];
    let mut cnt = vec![i64::MAX; n];

    let mut heap = std::collections::BinaryHeap::new();
    heap.push((0, 0, 0));

    while let Some((d, g, i)) = heap.pop() {
        let d = -d;
        if d >= dist[i] && g >= cnt[i] {
            continue;
        }
        if d < dist[i] {
            dist[i] = d;
        }
        cnt[i] = g;
        // println!("i:{i}, dist:{}, cnt:{g}, dist:{dist:?}", -d);
        // read_line();

        for &(j, c) in &edges[i] {
            if c == 0 {
                heap.push((-(d + 1), g, j));
            } else {
                heap.push((-(d + 1 + g), g + 1, j));
            }
        }
    }

    for &d in &dist {
        println!("{d}");
    }
}
