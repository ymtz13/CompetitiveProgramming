fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uuu() -> (usize, usize, usize) {
    let v = read_vec();
    (v[0], v[1], v[2])
}

trait Monoid {
    fn identity() -> Self;
    fn operate(self: &Self, rhs: &Self) -> Self;
}

trait Lazy {
    type TData;

    fn map(&self, data: &Self::TData, range: (usize, usize)) -> Self::TData;
    fn compose(&self, lazy: &Self) -> Self;
}

struct LazySegmentTree<TData, TLazy> {
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
    fn new(length: usize) -> LazySegmentTree<TData, TLazy> {
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

    fn update(&mut self, l: usize, r: usize, value: &TLazy) {
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

    fn query(&mut self, l: usize, r: usize) -> TData {
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

#[derive(Clone, Debug)]
struct Data(usize, usize, usize);

impl Monoid for Data {
    fn identity() -> Data {
        Data(0, 0, 0)
    }

    fn operate(&self, rhs: &Data) -> Data {
        Data(self.0 + rhs.0, self.1 + rhs.1, self.2 + rhs.2)
    }
}

impl Lazy for i8 {
    type TData = Data;

    fn map(&self, data: &Self::TData, (l, r): (usize, usize)) -> Data {
        let s = r - l;
        match self {
            -1 => Data(s, 0, 0),
            0 => Data(0, s, 0),
            1 => Data(0, 0, s),
            _ => panic!(),
        }
    }

    fn compose(&self, lazy: &Self) -> Self {
        *lazy
    }
}

fn main() {
    let (n, q, x) = read_uuu();
    let pp = read_vec();

    let mut lst = LazySegmentTree::new(n);

    for i in 0..n {
        let p = pp[i];

        let v = if p < x {
            -1
        } else if p > x {
            1
        } else {
            0
        };

        lst.update(i, i + 1, &v);
    }

    for _ in 0..q {
        let (c, l, r) = read_uuu();

        let Data(xm1, x0, xp1) = lst.query(l - 1, r);

        if c == 1 {
            if xm1 > 0 {
                lst.update(l - 1, l - 1 + xm1, &-1);
            }
            if x0 > 0 {
                lst.update(l - 1 + xm1, l - 1 + xm1 + x0, &0);
            }
            if xp1 > 0 {
                lst.update(l - 1 + xm1 + x0, r, &1);
            }
        } else {
            if xp1 > 0 {
                lst.update(l - 1, l - 1 + xp1, &1);
            }
            if x0 > 0 {
                lst.update(l - 1 + xp1, l - 1 + xp1 + x0, &0);
            }
            if xm1 > 0 {
                lst.update(l - 1 + xp1 + x0, r, &-1);
            }
        }
    }

    for i in 0..n {
        let Data(_, x0, _) = lst.query(i, i + 1);
        if x0 > 0 {
            println!("{}", i + 1);
        }
    }
}
