struct SegmentTree<T, F> {
    layers: Vec<Vec<T>>,
    function: F,
}

impl<T, F> std::fmt::Debug for SegmentTree<T, F>
where
    T: std::fmt::Debug,
{
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        writeln!(f, "SegTree {{")?;
        for (i, layer) in self.layers.iter().enumerate() {
            writeln!(f, "  {} : {:?}", i, layer)?;
        }
        // writeln!(f, "{:?}", self.layers)?;
        write!(f, "}}")
    }
}

impl<T, F> SegmentTree<T, F>
where
    T: std::clone::Clone,
    F: Fn(&T, &T) -> T,
{
    fn new(length: usize, identity: &T, function: F) -> SegmentTree<T, F> {
        let mut layers = Vec::new();
        let mut n = 1;
        loop {
            layers.push(vec![identity.clone(); n]);
            if n >= length {
                break;
            }
            n *= 2;
        }

        SegmentTree { layers, function }
    }

    fn update(&mut self, i: usize, value: T) {
        let mut i = i;
        let layers = &mut self.layers;

        if let Some(last) = layers.last_mut() {
            last[i] = value;
        }

        for l in (0..layers.len() - 1).rev() {
            i >>= 1;
            // layers[l][i] = std::cmp::max(layers[l + 1][i * 2], layers[l + 1][i * 2 + 1]);
            layers[l][i] = (self.function)(&layers[l + 1][i * 2], &layers[l + 1][i * 2 + 1]);
        }
    }

    fn query(&self, bgn: usize, end: usize) -> T {
        return self.query_inner(bgn, end, 0);
    }

    fn query_inner(&self, bgn: usize, end: usize, l: usize) -> T {
        let n = self.layers.last().unwrap().len();
        let segsize = n >> l;

        if bgn % segsize == 0 && bgn + segsize == end {
            return self.layers[l][bgn / segsize].clone();
        }

        let mid = (bgn / segsize) * segsize + segsize / 2;

        if (end <= mid) || (mid <= bgn) {
            return self.query_inner(bgn, end, l + 1);
        }

        let lvalue = self.query_inner(bgn, mid, l + 1);
        let rvalue = self.query_inner(mid, end, l + 1);

        // return std::cmp::max(lvalue, rvalue);
        return (self.function)(&lvalue, &rvalue);
    }
}

fn main() {
    let mut st = SegmentTree::new(7, &0, |&l, &r| std::cmp::max(l, r));
    st.update(3, 12);
    // [0, 0, 0, 3, 0, 0, 0]

    println!("{:?}", st);

    assert_eq!(st.query(0, 8), 12);
    assert_eq!(st.query(0, 7), 12);
    assert_eq!(st.query(1, 8), 12);
    assert_eq!(st.query(0, 4), 12);
    assert_eq!(st.query(0, 3), 0);
    assert_eq!(st.query(4, 8), 0);

    let mut st = SegmentTree::new(7, &0, |&l, &r| l + r);
    st.update(3, 4);
    st.update(6, 9);
    st.update(2, 1);
    st.update(1, 3);
    // [0, 3, 1, 4, 0, 0, 9]

    println!("{:?}", st);

    assert_eq!(st.query(0, 2), 3);
    assert_eq!(st.query(1, 3), 4);
    assert_eq!(st.query(1, 4), 8);
    assert_eq!(st.query(2, 5), 5);
}
