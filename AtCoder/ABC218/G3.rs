mod segtree {
    pub trait Monoid {
        fn identity() -> Self;
        fn operate(self: &Self, rhs: &Self) -> Self;
    }

    pub struct SegmentTree<T> {
        data: Vec<T>,
        depth: usize,
    }

    use std::fmt::{Debug, Formatter, Result};
    impl<T: Debug> Debug for SegmentTree<T> {
        fn fmt(&self, f: &mut Formatter<'_>) -> Result {
            writeln!(f, "SegTree {{")?;
            for d in 0..self.depth {
                let l = 1 << d;
                let layer = &self.data[l..l << 1];
                writeln!(f, "{d:>2} : {layer:?}")?;
            }
            write!(f, "}}")
        }
    }

    impl SegmentTree {
        pub fn len(&self) -> usize {
            1 << (self.depth - 1)
        }
    }

    impl<T: std::clone::Clone + Monoid> SegmentTree<T> {
        pub fn new(length: usize) -> SegmentTree<T> {
            let depth = length.next_power_of_two().ilog2() as usize + 1;

            SegmentTree {
                data: vec![T::identity(); 1 << depth],
                depth,
            }
        }

        pub fn update(&mut self, i: usize, value: T) {
            let SegmentTree { data, depth } = self;
            let mut i = i + (1 << (*depth - 1));

            data[i] = value;

            for _ in 1..*depth {
                i = i >> 1;
                let j = i << 1;
                data[i] = T::operate(&data[j], &data[j + 1]);
            }
        }

        pub fn query(&self, l: usize, r: usize) -> T {
            let depth = self.depth;

            let mut l = l + (1 << (depth - 1));
            let mut r = r + (1 << (depth - 1));

            let mut ll = vec![];
            let mut rr = vec![];

            for _ in 0..depth {
                if r <= l {
                    break;
                }

                if l & 1 == 1 {
                    ll.push(l);
                    l += 1;
                }
                if r & 1 == 1 {
                    rr.push(r ^ 1);
                }

                l >>= 1;
                r >>= 1;
            }

            let mut ii = ll;
            ii.extend(rr.iter().rev());

            ii.iter().fold(T::identity(), |acc, &i| T::operate(&acc, &self.data[i]))
        }

        pub fn get(&mut self, i: usize) -> T {
            let depth = self.depth;
            let mut i = i + (1 << (depth - 1));
            self.data[i]
        }
    }
}

use segtree::*;

impl Monoid for usize {
    fn identity() -> Self {
        0
    }

    fn operate(&self, rhs: &Self) -> Self {
        self + rhs
    }
}

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

use std::collections::HashMap;

fn cnt(st: &mut SegmentTree<usize>) {
    let m = st.len();
    let total = st.query(0, m);

    if total % 2 == 0 {
    } else {
    }
}

fn dfs(edges: &Vec<Vec<usize>>, st: &mut SegmentTree<usize>, aa: &Vec<i64>, map: &HashMap<i64, usize>, scores: &mut Vec<i64>, i: usize) {
    let a = aa[i];
    let d = map.get(&a).unwrap();

    st.update(d, st.get(d) + 1);

    if i > 1 && edges[i].len() == 1 {
        scores[i] = score;
    } else {
        for &j in &edges[i] {
            dfs(edges, st, aa, map, scores, j);
        }
    }

    st.update(d, st.get(d) - 1);
}

fn main() {
    let n: usize = read_line().parse().unwrap();

    let mut aa = vec![0];
    aa.extend(read_vec());
    let aa = aa;

    let mut dd = aa.clone();
    dd.sort();
    dd.dedup();

    let mut map = HashMap::new();
    for i in 0..dd.len() {
        map.insert(dd[i], i);
    }

    println!("{map:?}");

    let mut edges = vec![vec![]; n + 1];
    for _ in 0..n - 1 {
        let uv = read_vec();
        let u = uv[0] as usize;
        let v = uv[1] as usize;

        edges[u].push(v);
        edges[v].push(u);
    }

    let mut st: segtree::SegmentTree<usize> = SegmentTree::new(dd.len());

    let inf = n + 10;

    use std::collections::VecDeque;
    let mut queue = VecDeque::from(vec![(1, 0)]);
    let mut depth = vec![inf; n + 1];
    let mut order = vec![];
    while let Some((i, d)) = queue.pop_back() {
        if depth[i] != inf {
            continue;
        }
        depth[i] = d;
        order.push(i);

        for &j in &edges[i] {
            queue.push_front((j, d + 1));
        }
    }

    println!("{depth:?}");
    println!("{order:?}");

    let mut ok = 2;
    let mut ng = 1_000_000_001;

    while ng - ok > 1 {
        let tgt = (ok + ng) / 2;

        let mut ss = vec![0; n + 1];

        for &i in order.iter().rev() {
            let d = depth[i];

            let mut cc = vec![];
            for &j in &edges[i] {
                if depth[j] < d {
                    continue;
                }

                cc.push(ss[j]);
            }
            cc.sort();

            ss[i] = if aa[i] >= tgt { 1 } else { -1 };

            if cc.len() > 0 {
                if d % 2 == 0 {
                    ss[i] += cc.iter().max().unwrap();
                } else {
                    ss[i] += cc.iter().min().unwrap();
                }
            }
        }

        if ss[1] >= 0 {}
    }

    println!("{ok}");
}
