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

impl segtree::Monoid for usize {
    fn identity() -> usize {
        0
    }

    fn operate(&self, rhs: &usize) -> usize {
        std::cmp::max(*self, *rhs)
    }
}

impl lazy_segtree::Monoid for usize {
    fn identity() -> usize {
        0
    }

    fn operate(&self, rhs: &usize) -> usize {
        std::cmp::max(*self, *rhs)
    }
}

impl lazy_segtree::Lazy for usize {
    type TData = usize;

    fn map(&self, data: &Self::TData, _range: (usize, usize)) -> Self {
        std::cmp::max(*self, *data)
    }

    fn compose(&self, lazy: &Self) -> Self {
        std::cmp::max(*self, *lazy)
    }
}

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_uu() -> (usize, usize) {
    let v: Vec<_> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    (v[0], v[1])
}

fn main() {
    let n = read_line().parse().unwrap();

    let mut lr = vec![];
    let mut vv = vec![0];
    for _ in 0..n {
        let (l, r) = read_uu();
        lr.push((l, r));
        vv.push(l - 1);
        vv.push(l);
        vv.push(r);
    }
    vv.sort();
    vv.dedup();

    let mut map = std::collections::HashMap::new();
    for i in 0..vv.len() {
        map.insert(vv[i], i);
    }

    let nn = vv.len();

    let mut st = segtree::SegmentTree::new(nn);
    let mut lst = lazy_segtree::LazySegmentTree::new(nn);

    let k = 1 << 30;

    for i in 0..n {
        let (l, r) = lr[i];
        let il = *map.get(&l).unwrap();
        let ir = *map.get(&r).unwrap();

        let m0: usize = st.query(0, il);
        let t = lst.query(il - 1, il);
        let m1 = if t > 0 { t - (k - l + 1) } else { 0 };

        let ml = std::cmp::max(m0, m1) + 1;
        let mr = ml + r - l;

        // println!("m0:{m0}, t:{t}, m1:{m1} ml:{ml} mr:{mr}");

        st.update(ir, mr);
        lst.update(il, ir + 1, &(ml + k - l));
    }

    println!("{}", st.query(0, nn));
}
