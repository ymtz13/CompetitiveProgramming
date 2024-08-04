use std::cmp::max;

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

impl Monoid for i64 {
    fn identity() -> i64 {
        0
    }

    fn operate(&self, rhs: &i64) -> i64 {
        std::cmp::max(*self, *rhs)
    }
}

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|s| s.parse().unwrap()).collect()
}

fn read_uu() -> (usize, usize) {
    let a = read_vec();
    (a[0], a[1])
}

fn main() {
    let (n, c) = read_uu();
    let m: usize = read_line().parse().unwrap();

    let mut tp = vec![];
    for _ in 0..m {
        tp.push(read_uu());
    }

    let mut sl = SegmentTree::new(n + 2);
    let mut sr = SegmentTree::new(n + 2);

    for &(t, p) in tp.iter().rev() {
        let ql: i64 = sl.query(0, t + 1);
        let qr: i64 = sr.query(t, n + 2);

        let ol = (c * t) as i64;
        let or = (c * (n - t)) as i64;

        let dl = ql - ol;
        let dr = qr - or;

        let pp = p as i64 + max(0, max(dl, dr));

        sl.update(t, pp + ol);
        sr.update(t, pp + or);
    }

    let ql = sl.query(0, 2);
    let qr = sr.query(2, n + 2);

    let dl = ql - c as i64;
    let dr = qr - (c * (n - 1)) as i64;

    let ans = max(0, max(dl, dr));

    println!("{ans}");
}
