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
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn solve(n: usize, aa: Vec<usize>) -> Vec<usize> {
    let mut dd = aa.clone();
    dd.sort();
    dd.dedup();
    dd.push(0);
    dd.push(1_000_000_005);

    let mut map = std::collections::HashMap::new();
    for i in 0..dd.len() {
        map.insert(dd[i], i);
    }

    let mut vl = vec![];
    let mut st_l = SegmentTree::new(dd.len());
    for &a in &aa {
        let i = *map.get(&a).unwrap();
        let v: i64 = st_l.query(0, i) + 1;
        st_l.update(i, v);
        vl.push(v);
    }

    let mut vr = vec![];
    let mut st_r = SegmentTree::new(dd.len());
    for &a in aa.iter().rev() {
        let i = *map.get(&a).unwrap();
        let v: i64 = st_r.query(i + 1, dd.len()) + 1;
        st_r.update(i, v);
        vr.push(v);
    }
    vr.reverse();

    let len = st_r.query(0, dd.len());

    let mut ans = vec![];
    for i in 0..n {
        if vl[i] + vr[i] == len + 1 {
            ans.push(i + 1);
        }
    }

    ans
}

fn main() {
    let t: usize = read_line().parse().unwrap();

    for _ in 0..t {
        let n: usize = read_line().parse().unwrap();
        let aa = read_vec();

        let ans = solve(n, aa);

        println!("{}", ans.len());
        println!("{}", ans.into_iter().map(|v| v.to_string()).collect::<Vec<_>>().join(" "));
    }
}
