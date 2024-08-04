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

fn main() {
    let n = read_vec()[0] as usize;
    let mut edges = vec![vec![]; n + 1];

    for _ in 0..n - 1 {
        let (u, v) = read_uu();
        edges[u].push(v);
        edges[v].push(u);
    }

    let mut depth = vec![0; n + 1];
    let mut parent = vec![0; n + 1];
    let mut order = vec![];

    let mut queue = std::collections::VecDeque::new();
    queue.push_back((1, 0, 0));

    while let Some((i, d, p)) = queue.pop_front() {
        order.push(i);
        depth[i] = d;
        parent[i] = p;

        for &j in &edges[i] {
            if j == p {
                continue;
            }
            queue.push_back((j, d + 1, i));
        }
    }

    // println!("{order:?}");

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

    let mut r = 1;
    loop {
        let mut rnxt = 0;
        for &j in &edges[r] {
            if j == parent[r] {
                continue;
            }

            if size[j] * 2 > n {
                rnxt = j;
            }
        }

        if rnxt == 0 {
            break;
        }

        r = rnxt;
    }

    let mut ppp = vec![];
    for &i in &edges[r] {
        let mut pp = vec![];

        let mut queue = std::collections::VecDeque::new();
        queue.push_back((i, r));

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

    if n % 2 == 0 {
        for i in 0..ppp.len() {
            if ppp[i].len() * 2 < n {
                ppp[i].push(r);
                break;
            }
        }
    }

    // println!("{r} {ppp:?}");

    let mut heap = std::collections::BinaryHeap::new();
    for i in 0..ppp.len() {
        heap.push((ppp[i].len(), i));
    }

    while let Some((_, i)) = heap.pop() {
        let (_, j) = heap.pop().unwrap();

        // let ppi = &mut ppp[i];
        // let ppj = &mut ppp[j];

        let a = ppp[i].pop().unwrap();
        let b = ppp[j].pop().unwrap();

        println!("{a} {b}");

        if ppp[i].len() > 0 {
            heap.push((ppp[i].len(), i));
        }
        if ppp[j].len() > 0 {
            heap.push((ppp[j].len(), j));
        }
    }
}
