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

impl Monoid for (i64, usize) {
    fn identity(index: usize) -> Self {
        (0, index)
    }

    fn operate(&self, rhs: &Self) -> Self {
        if self.0 < rhs.0 {
            return *rhs;
        }
        *self
    }
}

impl Lazy for i64 {
    type TData = (i64, usize);

    fn map(&self, data: &Self::TData, _range: (usize, usize)) -> Self::TData {
        (*self + data.0, data.1)
    }

    fn compose(&self, lazy: &Self) -> Self {
        *self + *lazy
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

fn main() {
    let n = read_vec()[0];
    let mut lr = vec![];
    let mut vv = vec![0];
    for _ in 0..n {
        let v = read_vec();
        let l = v[0];
        let r = v[1];
        lr.push((l, r));
        vv.push(l);
        vv.push(l + 1);
        vv.push(r);
        if r < 1_000_000_000 {
            vv.push(r + 1);
        }
    }

    vv.sort();
    vv.dedup();
    let m = vv.len();

    let mut map = std::collections::HashMap::new();
    for i in 0..m {
        map.insert(vv[i], i);
    }

    let mut ee = vec![vec![]; m + 1];
    let mut xlr = vec![];
    for i in 0..n {
        let (l, r) = lr[i];
        let jl = *map.get(&l).unwrap();
        let jm = *map.get(&(l + 1)).unwrap();
        let jr = *map.get(&r).unwrap();

        ee[jl].push((0, i));
        ee[jm].push((1, i));
        ee[jr].push((2, i));
        xlr.push((jl, jr));
    }

    let mut st = LazySegmentTree::new(m + 1);
    for &(l, r) in &xlr {
        st.update(l + 1, r, &1);
    }

    let mut ans = (0, 0, 1);
    for l in 0..m - 1 {
        for &(t, i) in &ee[l] {
            let (l, r) = xlr[i];
            if t == 0 {
                st.update(l + 1, r, &(-1));
            }
            if t == 1 {
                st.update(r + 1, m, &1);
            }
            if t == 2 {
                st.update(r + 1, m, &(-1));
            }
        }

        let z = st.query(l + 1, m);

        if z.0 > ans.0 {
            ans = (z.0, l, z.1);
        }

        // println!("{st:?}");
    }

    println!("{} {}", vv[ans.1], vv[ans.2]);
}
