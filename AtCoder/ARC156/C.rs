fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_uu() -> (usize, usize) {
    let v: Vec<_> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    (v[0], v[1])
}

fn main() {
    let n: usize = read_line().parse().unwrap();

    let mut edges = vec![vec![]; n + 1];
    for _ in 1..n {
        let (u, v) = read_uu();
        edges[u].push(v);
        edges[v].push(u);
    }

    if n == 2 {
        println!("2 1");
        return;
    }

    let mut parent = vec![0; n + 1];
    let mut order = vec![];
    let mut queue = std::collections::VecDeque::new();
    queue.push_back((1, 0));
    while let Some((i, p)) = queue.pop_front() {
        parent[i] = p;
        order.push(i);

        for &j in &edges[i] {
            if j == p {
                continue;
            }
            queue.push_back((j, i));
        }
    }

    let mut size = vec![0; n + 1];
    for &i in order.iter().rev() {
        let mut s = 1;
        for &j in &edges[i] {
            if j == parent[i] {
                continue;
            }
            s += size[j];
        }
        size[i] = s;
    }

    let mut g = 1;
    loop {
        let mut gnxt = 0;
        for &j in &edges[g] {
            if j == parent[g] {
                continue;
            }
            if size[j] * 2 > n {
                gnxt = j;
            }
        }

        if gnxt == 0 {
            break;
        }

        g = gnxt;
    }

    let mut ppp = vec![];
    for &s in &edges[g] {
        let mut pp = vec![];
        let mut queue = std::collections::VecDeque::new();
        queue.push_back((s, g));
        while let Some((i, p)) = queue.pop_front() {
            pp.push(i);

            for &j in &edges[i] {
                if j == p {
                    continue;
                }
                queue.push_back((j, i));
            }
        }

        ppp.push(pp);
    }

    let mut heap = std::collections::BinaryHeap::new();
    for i in 0..ppp.len() {
        heap.push((ppp[i].len(), i));
    }

    let mut sw = vec![];
    loop {
        let (ci, i) = heap.pop().unwrap();
        let (cj, j) = heap.pop().unwrap();

        if ci == 0 || cj == 0 {
            if ci > 0 {
                let ai = ppp[i].pop().unwrap();
                sw.push((ai, g));
            }
            break;
        }

        heap.push((ci - 1, i));
        heap.push((cj - 1, j));

        let ai = ppp[i].pop().unwrap();
        let aj = ppp[j].pop().unwrap();
        sw.push((ai, aj));
    }

    let mut ans = vec![0; n + 1];
    ans[g] = g;
    for &(ai, aj) in &sw {
        ans[aj] = ai;
        ans[ai] = aj;
    }

    let mut aans = vec![];
    for &a in &ans[1..] {
        aans.push(a.to_string());
    }

    println!("{}", aans.join(" "));
}
