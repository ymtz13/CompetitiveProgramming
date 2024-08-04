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

impl Monoid for usize {
    fn identity() -> Self {
        0
    }

    fn operate(&self, rhs: &Self) -> Self {
        self + rhs
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
    read_line();

    let m = 1000010;

    let aa = read_vec();
    let mut cc = vec![0; m];
    for &a in &aa {
        cc[a] += 1;
    }

    let mut st = SegmentTree::<usize>::new(m);
    let mut ans = 0;

    for a in (0..m).rev() {
        let c = cc[a];
        if c == 0 {
            continue;
        }
        ans += c * (c - 1) / 2;

        for d in 1..m {
            if a * d > m {
                break;
            }

            let v = st.query(a * d, std::cmp::min(m, a * (d + 1)));
            ans += c * d * v;
        }

        st.update(a, st.query(a, a + 1) + c);
    }

    println!("{ans}");
}
