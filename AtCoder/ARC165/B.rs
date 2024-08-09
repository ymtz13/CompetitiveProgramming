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
    }
}

use segtree::*;

impl Monoid for usize {
    fn identity() -> Self {
        usize::MAX
    }

    fn operate(&self, rhs: &Self) -> Self {
        std::cmp::min(*self, *rhs)
    }
}

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn printans(aa: &[usize]) {
    println!("{}", aa.iter().map(|c| c.to_string()).collect::<Vec<_>>().join(" "));
}

fn main() {
    let nk = read_vec();
    let n = nk[0];
    let k = nk[1];
    let mut pp = read_vec();
    pp.push(0);

    let mut st = SegmentTree::new(n);
    let mut heap = std::collections::BinaryHeap::new();
    let mut zz = vec![vec![]; n + 1];

    for i in 0..=n {
        let p = pp[i];
        while let Some((q, j)) = heap.pop() {
            if q < p {
                heap.push((q, j));
                break;
            }
            zz[i].push(j);
        }
        heap.push((p, i));
    }

    // println!("{zz:?}");

    for i in 0..k {
        for &j in &zz[i] {
            st.update(j, j);
        }
    }

    let mut ans = (0, 0);
    for i in 0..=n - k {
        let v = st.query(i, i + k);

        if v == usize::MAX {
            printans(&pp[..n]);
            return;
        }

        if v > ans.0 {
            ans = (v, i);
        }

        // ans = std::cmp::max(ans, (v, i));

        for &j in &zz[i + k] {
            st.update(j, j);
        }

        // println!("{st:?}");
    }

    // println!("{ans:?}");

    let i = ans.1;
    pp[i..i + k].sort();
    printans(&pp[..n]);
}
