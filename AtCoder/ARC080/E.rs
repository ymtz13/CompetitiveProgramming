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

impl Monoid for (usize, usize) {
    fn identity() -> Self {
        (usize::MAX, 0)
    }

    fn operate(&self, rhs: &Self) -> Self {
        if self.0 < rhs.0 {
            *self
        } else {
            *rhs
        }
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

use std::collections::BinaryHeap;

fn main() {
    let n = read_vec()[0];
    let m = n / 2;
    let pp = read_vec();

    let mut st0 = SegmentTree::new(n + 5);
    let mut st1 = SegmentTree::new(n + 5);

    for i in 0..m {
        st0.update(i * 2, (pp[i * 2], i * 2));
        st1.update(i * 2 + 1, (pp[i * 2 + 1], i * 2 + 1));
    }

    let mut ans = vec![];
    let mut heap = BinaryHeap::new();

    heap.push(((0, 0), 0, n, n + 1, n + 2));

    while let Some((v, ll, il, ir, rr)) = heap.pop() {
        ans.push(v);

        let mut push = |l: usize, r: usize| {
            if l >= r {
                return;
            }

            let (st0, st1) = if l % 2 == 0 { (&st0, &st1) } else { (&st1, &st0) };

            let m0 = st0.query(l, r);
            let m1 = st1.query(m0.1, r);

            heap.push(((-(m0.0 as i64), -(m1.0 as i64)), l, m0.1, m1.1, r));
        };

        push(ll, il);
        push(il + 1, ir);
        push(ir + 1, rr);
    }

    let mut aa = vec![];
    for &(a1, a2) in &ans[1..] {
        aa.push((-a1).to_string());
        aa.push((-a2).to_string());
    }

    println!("{}", aa.join(" "));
}
