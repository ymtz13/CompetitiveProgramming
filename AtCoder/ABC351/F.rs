trait Monoid {
    fn identity() -> Self;
    fn operate(self: &Self, rhs: &Self) -> Self;
}

struct SegmentTree<T> {
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
    fn new(length: usize) -> SegmentTree<T> {
        let depth = length.next_power_of_two().ilog2() as usize + 1;

        SegmentTree {
            data: vec![T::identity(); 1 << depth],
            depth,
        }
    }

    fn update(&mut self, i: usize, value: T) {
        let SegmentTree { data, depth } = self;
        let mut i = i + (1 << (*depth - 1));

        data[i] = value;

        for _ in 1..*depth {
            i = i >> 1;
            let j = i << 1;
            data[i] = T::operate(&data[j], &data[j + 1]);
        }
    }

    fn query(&self, l: usize, r: usize) -> T {
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

impl Monoid for (i64, i64) {
    fn identity() -> (i64, i64) {
        (0, 0)
    }

    fn operate(&self, rhs: &(i64, i64)) -> (i64, i64) {
        (self.0 + rhs.0, self.1 + rhs.1)
    }
}

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let aa = read_vec();

    let mut bb = aa.clone();
    bb.sort();
    bb.dedup();

    let mut map = std::collections::HashMap::new();
    for i in 0..bb.len() {
        map.insert(bb[i], i);
    }

    let mut st = SegmentTree::new(bb.len());
    let mut ans = 0;

    let mut cc = vec![0; bb.len()];

    for &a in &aa {
        let i = *map.get(&a).unwrap();

        if i > 0 {
            let (cnt, sum) = st.query(0, i);
            ans += cnt * a - sum;
        }

        cc[i] += 1;

        st.update(i, (cc[i], cc[i] * a));
    }

    println!("{ans}");
}
