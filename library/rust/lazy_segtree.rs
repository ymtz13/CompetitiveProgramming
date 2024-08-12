mod lazy_segtree {
    pub trait Monoid {
        fn identity(index: usize) -> Self;
        fn operate(self: &Self, rhs: &Self) -> Self;
    }

    pub trait Lazy {
        type TData;

        fn map(&self, data: &Self::TData, range: (usize, usize)) -> Self::TData;
        fn compose(&self, lazy: &Self) -> Self;
    }

    pub struct LazySegmentTree<TData, TLazy> {
        data: Vec<TData>,
        lazy: Vec<Option<TLazy>>,
        depth: usize,
    }

    use std::fmt::{Debug, Formatter, Result};
    impl<TData: Debug, TLazy> Debug for LazySegmentTree<TData, TLazy> {
        fn fmt(&self, f: &mut Formatter<'_>) -> Result {
            writeln!(f, "LazySegTree {{")?;
            for d in 0..self.depth {
                let l = 1 << d;
                let layer = &self.data[l..l << 1];
                writeln!(f, "{d:>2} : {layer:?}")?;
            }
            write!(f, "}}")
        }
    }

    use std::clone::Clone;
    impl<TData: Clone + Monoid, TLazy: Clone + Lazy<TData = TData>> LazySegmentTree<TData, TLazy> {
        pub fn new(length: usize) -> LazySegmentTree<TData, TLazy> {
            let depth = length.next_power_of_two().ilog2() as usize + 1;

            let len = 1 << (depth - 1);

            let mut data = vec![TData::identity(0); len];

            for i in 0..len {
                data.push(TData::identity(i));
            }

            for i in (1..len).rev() {
                let j = i << 1;
                data[i] = TData::operate(&data[j], &data[j + 1]);
            }

            LazySegmentTree {
                data,
                lazy: vec![None; 1 << depth],
                depth,
            }
        }

        fn set_lazy(&mut self, i: usize, value: &TLazy) {
            if i >= self.lazy.len() {
                return;
            }

            if let Some(current) = &self.lazy[i] {
                self.lazy[i] = Some(Lazy::compose(&current, value));
            } else {
                self.lazy[i] = Some(value.clone());
            }
        }

        fn resolve(&mut self, i: usize) {
            if let Some(value) = self.lazy[i].clone() {
                let j = i << 1;
                self.set_lazy(j, &value);
                self.set_lazy(j | 1, &value);

                let d = i.ilog2() as usize;
                let segment_size = 1 << (self.depth - 1 - d);
                let l = (i - (1 << d)) * segment_size;
                let r = l + segment_size;

                self.data[i] = Lazy::map(&value, &self.data[i], (l, r));
                self.lazy[i] = None;
            }
        }

        fn segments(&self, l: usize, r: usize) -> Vec<usize> {
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

            ii
        }

        fn ancestors(&self, l: usize, r: usize) -> Vec<usize> {
            let mut ret = vec![];

            for d in 0..self.depth {
                let segment_size = 1 << (self.depth - 1 - d);
                let i0 = 1 << d;

                if l % segment_size != 0 {
                    let i = i0 + l / segment_size;
                    ret.push(i);
                }

                if r % segment_size != 0 {
                    let i = i0 + r / segment_size;
                    if !ret.last().is_some_and(|&last| last == i) {
                        ret.push(i);
                    }
                }
            }

            ret
        }

        pub fn update(&mut self, l: usize, r: usize, value: &TLazy) {
            let segments = self.segments(l, r);
            let ancestors = self.ancestors(l, r);

            for &i in &ancestors {
                self.resolve(i);
            }

            for &i in &segments {
                self.set_lazy(i, value);
            }

            for &i in ancestors.iter().rev() {
                let j = i << 1;
                self.resolve(j);
                self.resolve(j | 1);
                self.data[i] = TData::operate(&self.data[j], &self.data[j | 1]);
            }
        }

        pub fn query(&mut self, l: usize, r: usize) -> TData {
            let segments = self.segments(l, r);
            let ancestors = self.ancestors(l, r);

            for &i in &ancestors {
                self.resolve(i);
            }

            for &i in &segments {
                self.resolve(i);
            }

            segments
                .iter()
                .map(|&i| self.data[i].clone())
                .reduce(|acc, data| TData::operate(&acc, &data))
                .unwrap()
        }
    }
}

use lazy_segtree::*;

impl Monoid for i64 {
    fn identity(_: usize) -> Self {
        0
    }

    fn operate(&self, rhs: &Self) -> Self {
        std::cmp::max(*self, *rhs)
    }
}

impl Lazy for i64 {
    type TData = i64;

    fn map(&self, data: &Self::TData, _range: (usize, usize)) -> Self::TData {
        *self + *data
    }

    fn compose(&self, lazy: &Self) -> Self {
        *self + *lazy
    }
}

fn main() {
    let n = 7;
    let mut st = LazySegmentTree::new(n);
    st.update(2, 5, &12);

    let naive = vec![0, 0, 12, 12, 12, 0, 0];

    println!("{:?}", st);

    for l in 0..n {
        for r in l + 1..n {
            assert_eq!(st.query(l, r), *naive[l..r].into_iter().max().unwrap());
        }
    }

    assert_eq!(st.query(0, 7), 12);
    assert_eq!(st.query(1, 8), 12);
    assert_eq!(st.query(0, 4), 12);
    assert_eq!(st.query(0, 3), 12);
    assert_eq!(st.query(4, 8), 12);
}