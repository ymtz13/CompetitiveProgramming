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

        pub fn get(&mut self, i: usize) -> T {
            let depth = self.depth;
            let mut i = i + (1 << (depth - 1));
            self.data[i]
        }
    }
}

use segtree::*;

impl Monoid for i64 {
    fn identity() -> Self {
        0
    }

    fn operate(&self, rhs: &Self) -> Self {
        std::cmp::max(*self, *rhs)
    }
}

impl Monoid for (i64, i64) {
    fn identity() -> Self {
        (0, 0)
    }

    fn operate(&self, rhs: &Self) -> Self {
        (self.0 + rhs.0, self.1 + rhs.1)
    }
}

fn main() {
    let mut st = SegmentTree::new(7);
    st.update(3, 12);
    // [0, 0, 0, 12, 0, 0, 0]

    println!("{:?}", st);

    assert_eq!(st.query(0, 8), 12);
    assert_eq!(st.query(0, 7), 12);
    assert_eq!(st.query(1, 8), 12);
    assert_eq!(st.query(0, 4), 12);
    assert_eq!(st.query(0, 3), 0);
    assert_eq!(st.query(4, 8), 0);

    let mut st = SegmentTree::new(7);
    st.update(3, (4, 1));
    st.update(6, (9, 2));
    st.update(2, (1, 3));
    st.update(1, (3, 4));
    // [0, 3, 1, 4, 0, 0, 9]

    println!("{:?}", st);

    assert_eq!(st.query(0, 2).0, 3);
    assert_eq!(st.query(1, 3).0, 4);
    assert_eq!(st.query(1, 4).0, 8);
    assert_eq!(st.query(2, 5).0, 5);
}
