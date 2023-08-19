const INF: i64 = 1_000_000_000;

fn main() {
    let (n,): (usize,) = Read::read();
    let plist: Vec<_> = input()
        .split_whitespace()
        .map(|c| c.parse::<i64>().unwrap())
        .enumerate()
        .collect();
    let mut plist: Vec<_> = plist.iter().map(|&(i, v)| (i + 1, v)).collect();
    plist.sort_by_key(|v| v.1);
    // println!("{} {:?}", n, plist);

    let mut st_l_lt = SegmentTree::new(n + 2, &INF, |&l, &r| std::cmp::min(l, r)); // (-Pj -j) +Pi +i
    let mut st_l_gt = SegmentTree::new(n + 2, &INF, |&l, &r| std::cmp::min(l, r)); // (+Pj -j) -Pi +i
    let mut st_r_lt = SegmentTree::new(n + 2, &INF, |&l, &r| std::cmp::min(l, r)); // (-Pj +j) +Pi -i
    let mut st_r_gt = SegmentTree::new(n + 2, &INF, |&l, &r| std::cmp::min(l, r)); // (+Pj +j) -Pi -i

    for &(i, p) in &plist {
        st_l_gt.update(i, p - i as i64);
        st_r_gt.update(i, p + i as i64);
    }

    let mut anslist = vec![INF; n];

    for &(i, pi) in &plist {
        let v_l_lt = st_l_lt.query(0, i);
        let v_l_gt = st_l_gt.query(0, i);
        let v_r_lt = st_r_lt.query(i + 1, n + 2);
        let v_r_gt = st_r_gt.query(i + 1, n + 2);

        // println!("(i, pi) = ({i}, {pi})");
        // println!(
        //     "{:?}\n{:?}\n{:?}\n{:?}\n",
        //     st_l_lt, st_l_gt, st_r_lt, st_r_gt
        // );

        let vlist = vec![
            v_l_lt + pi + i as i64,
            v_l_gt - pi + i as i64,
            v_r_lt + pi - i as i64,
            v_r_gt - pi - i as i64,
        ];

        let ans = *vlist.iter().min().unwrap();
        anslist[i - 1] = ans;

        st_l_gt.update(i, INF);
        st_r_gt.update(i, INF);
        st_l_lt.update(i, -pi - i as i64);
        st_r_lt.update(i, -pi + i as i64);
    }

    println!(
        "{}",
        anslist
            .iter()
            .map(|c| c.to_string())
            .collect::<Vec<_>>()
            .join(" ")
    );
}

//=============================================================================

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

trait Read {
    fn read() -> Self;
}

impl<T1> Read for (T1,)
where
    T1: std::str::FromStr,
{
    fn read() -> (T1,) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();

        if let Ok(v1) = v1 {
            return (v1,);
        }

        panic!();
    }
}

impl<T1, T2> Read for (T1, T2)
where
    T1: std::str::FromStr,
    T2: std::str::FromStr,
{
    fn read() -> (T1, T2) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();
        let v2 = s.next().unwrap().parse();

        if let (Ok(v1), Ok(v2)) = (v1, v2) {
            return (v1, v2);
        }

        panic!();
    }
}

impl<T1, T2, T3> Read for (T1, T2, T3)
where
    T1: std::str::FromStr,
    T2: std::str::FromStr,
    T3: std::str::FromStr,
{
    fn read() -> (T1, T2, T3) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();
        let v2 = s.next().unwrap().parse();
        let v3 = s.next().unwrap().parse();

        if let (Ok(v1), Ok(v2), Ok(v3)) = (v1, v2, v3) {
            return (v1, v2, v3);
        }

        panic!();
    }
}

impl<T1, T2, T3, T4> Read for (T1, T2, T3, T4)
where
    T1: std::str::FromStr,
    T2: std::str::FromStr,
    T3: std::str::FromStr,
    T4: std::str::FromStr,
{
    fn read() -> (T1, T2, T3, T4) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();
        let v2 = s.next().unwrap().parse();
        let v3 = s.next().unwrap().parse();
        let v4 = s.next().unwrap().parse();

        if let (Ok(v1), Ok(v2), Ok(v3), Ok(v4)) = (v1, v2, v3, v4) {
            return (v1, v2, v3, v4);
        }

        panic!();
    }
}

impl<T1, T2, T3, T4, T5> Read for (T1, T2, T3, T4, T5)
where
    T1: std::str::FromStr,
    T2: std::str::FromStr,
    T3: std::str::FromStr,
    T4: std::str::FromStr,
    T5: std::str::FromStr,
{
    fn read() -> (T1, T2, T3, T4, T5) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();
        let v2 = s.next().unwrap().parse();
        let v3 = s.next().unwrap().parse();
        let v4 = s.next().unwrap().parse();
        let v5 = s.next().unwrap().parse();

        if let (Ok(v1), Ok(v2), Ok(v3), Ok(v4), Ok(v5)) = (v1, v2, v3, v4, v5) {
            return (v1, v2, v3, v4, v5);
        }

        panic!();
    }
}

impl<T1, T2, T3, T4, T5, T6> Read for (T1, T2, T3, T4, T5, T6)
where
    T1: std::str::FromStr,
    T2: std::str::FromStr,
    T3: std::str::FromStr,
    T4: std::str::FromStr,
    T5: std::str::FromStr,
    T6: std::str::FromStr,
{
    fn read() -> (T1, T2, T3, T4, T5, T6) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();
        let v2 = s.next().unwrap().parse();
        let v3 = s.next().unwrap().parse();
        let v4 = s.next().unwrap().parse();
        let v5 = s.next().unwrap().parse();
        let v6 = s.next().unwrap().parse();

        if let (Ok(v1), Ok(v2), Ok(v3), Ok(v4), Ok(v5), Ok(v6)) = (v1, v2, v3, v4, v5, v6) {
            return (v1, v2, v3, v4, v5, v6);
        }

        panic!();
    }
}

struct SegmentTree<T, F> {
    layers: Vec<Vec<T>>,
    function: F,
}

impl<T, F> std::fmt::Debug for SegmentTree<T, F>
where
    T: std::fmt::Debug,
{
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        writeln!(f, "SegTree {{")?;
        for (i, layer) in self.layers.iter().enumerate() {
            writeln!(f, "  {} : {:?}", i, layer)?;
        }
        // writeln!(f, "{:?}", self.layers)?;
        write!(f, "}}")
    }
}

impl<T, F> SegmentTree<T, F>
where
    T: std::clone::Clone,
    F: Fn(&T, &T) -> T,
{
    fn new(length: usize, identity: &T, function: F) -> SegmentTree<T, F> {
        let mut layers = Vec::new();
        let mut n = 1;
        loop {
            layers.push(vec![identity.clone(); n]);
            if n >= length {
                break;
            }
            n *= 2;
        }

        SegmentTree { layers, function }
    }

    fn update(&mut self, i: usize, value: T) {
        let mut i = i;
        let layers = &mut self.layers;

        if let Some(last) = layers.last_mut() {
            last[i] = value;
        }

        for l in (0..layers.len() - 1).rev() {
            i >>= 1;
            // layers[l][i] = std::cmp::max(layers[l + 1][i * 2], layers[l + 1][i * 2 + 1]);
            layers[l][i] = (self.function)(&layers[l + 1][i * 2], &layers[l + 1][i * 2 + 1]);
        }
    }

    fn query(&self, bgn: usize, end: usize) -> T {
        return self.query_inner(bgn, end, 0);
    }

    fn query_inner(&self, bgn: usize, end: usize, l: usize) -> T {
        let n = self.layers.last().unwrap().len();
        let segsize = n >> l;

        if bgn % segsize == 0 && bgn + segsize == end {
            return self.layers[l][bgn / segsize].clone();
        }

        let mid = (bgn / segsize) * segsize + segsize / 2;

        if (end <= mid) || (mid <= bgn) {
            return self.query_inner(bgn, end, l + 1);
        }

        let lvalue = self.query_inner(bgn, mid, l + 1);
        let rvalue = self.query_inner(mid, end, l + 1);

        // return std::cmp::max(lvalue, rvalue);
        return (self.function)(&lvalue, &rvalue);
    }
}
