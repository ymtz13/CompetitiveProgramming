mod lazy_segtree {
    pub trait Monoid {
        fn identity() -> Self;
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

            LazySegmentTree {
                data: vec![TData::identity(); 1 << depth],
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

            segments.iter().fold(TData::identity(), |acc, &i| TData::operate(&acc, &self.data[i]))
        }
    }
}

const MOD: u128 = 998244353;

use lazy_segtree::*;

impl Monoid for (u128, u128, u128) {
    fn identity() -> Self {
        (0, 0, 0)
    }

    fn operate(&self, rhs: &Self) -> Self {
        let v0 = (self.0 + rhs.0) % MOD;
        let v1 = (self.1 + rhs.1) % MOD;
        let v2 = (self.2 + rhs.2) % MOD;
        (v0, v1, v2)
    }
}

impl Lazy for (u128, u128) {
    type TData = (u128, u128, u128);

    fn map(&self, data: &Self::TData, (l, r): (usize, usize)) -> Self::TData {
        let &(sa, sb, sab) = data;
        let &(da, db) = self;
        let n = (r - l) as u128;

        ((sa + n * da) % MOD, (sb + n * db) % MOD, (sab + sa * db + sb * da + n * da * db) % MOD)
    }

    fn compose(&self, lazy: &Self) -> Self {
        let &(da, db) = self;
        let &(ea, eb) = lazy;
        (da + ea, db + eb)
    }
}

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<u128> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (u128, u128) {
    let v = read_vec();
    (v[0], v[1])
}

fn main() {
    let (n, q) = read_uu();
    let aa = read_vec();
    let bb = read_vec();

    let mut st = LazySegmentTree::new(n as usize);

    for i in 0..(n as usize) {
        let a = aa[i];
        let b = bb[i];
        st.update(i, i + 1, &(a, b));
    }

    for _ in 0..(q as usize) {
        let query = read_vec();
        let t = query[0];

        if t == 1 {
            let l = query[1] as usize;
            let r = query[2] as usize;
            let x = query[3];
            st.update(l - 1, r, &(x, 0));
        }
        if t == 2 {
            let l = query[1] as usize;
            let r = query[2] as usize;
            let x = query[3];
            st.update(l - 1, r, &(0, x));
        }
        if t == 3 {
            let l = query[1] as usize;
            let r = query[2] as usize;
            let ans = st.query(l - 1, r);

            println!("{}", ans.2);
        }
    }
}
