mod pot_union_find {
    pub trait Group {
        fn identity() -> Self;

        fn operate(&self, rhs: &Self) -> Self;

        fn inverse(&self) -> Self;
    }

    #[derive(Clone)]
    enum Node {
        Root(usize),
        ChildOf(usize),
    }

    pub struct PotUnionFind<TGroup> {
        nodes: Vec<Node>,
        potentials: Vec<TGroup>,
        n: usize,
    }

    use std::clone::Clone;
    impl<TGroup: Clone + Group> PotUnionFind<TGroup> {
        pub fn new(length: usize) -> PotUnionFind<TGroup> {
            PotUnionFind {
                nodes: vec![Node::Root(1); length],
                potentials: vec![TGroup::identity(); length],
                n: length,
            }
        }

        pub fn find(&mut self, i: usize) -> usize {
            match self.nodes[i] {
                Node::Root(_) => i,
                Node::ChildOf(i_parent) => {
                    let i_root = self.find(i_parent);
                    self.nodes[i] = Node::ChildOf(i_root);
                    self.potentials[i] = TGroup::operate(&self.potentials[i_parent], &self.potentials[i]);
                    i_root
                }
            }
        }

        pub fn size(&mut self, i: usize) -> usize {
            let i_root = self.find(i);
            match self.nodes[i_root] {
                Node::Root(size) => size,
                _ => panic!(),
            }
        }

        pub fn union(&mut self, i: usize, j: usize, v: TGroup) {
            // pot[i] = op(pot[j], v)

            let mut i_root = self.find(i);
            let mut j_root = self.find(j);

            if i_root == j_root {
                return;
            }

            let pot_i = &self.potentials[i];
            let pot_j = &self.potentials[j];
            let mut v = pot_j.operate(&v).operate(&pot_i.inverse());

            let size_i = self.size(i_root);
            let size_j = self.size(j_root);

            if size_i > size_j {
                (i_root, j_root) = (j_root, i_root);
                v = v.inverse();
            }

            self.nodes[j_root] = Node::Root(size_i + size_j);
            self.nodes[i_root] = Node::ChildOf(j_root);
            self.potentials[i_root] = v;
            self.n -= 1;
        }

        pub fn components(&mut self) -> Vec<Vec<(usize, TGroup)>> {
            let mut map = std::collections::HashMap::new();

            let len = self.nodes.len();
            for i in 0..len {
                let i_root = self.find(i);
                let vv = map.entry(i_root).or_insert(vec![]);
                vv.push((i, self.potentials[i].clone()));
            }

            map.into_values().collect()
        }
    }
}

impl pot_union_find::Group for i64 {
    fn identity() -> i64 {
        0
    }

    fn operate(&self, &rhs: &i64) -> i64 {
        *self + rhs
    }

    fn inverse(&self) -> i64 {
        -*self
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

fn read_uu() -> (usize, usize) {
    let a = read_vec();
    (a[0], a[1])
}

fn read_uui() -> (usize, usize, i64) {
    let a = read_vec();
    (a[0], a[1], a[2] as i64)
}

const NONE: usize = 20;

fn dfs(n: usize, res: &mut Vec<Vec<usize>>, cc2: &Vec<Vec<(usize, usize)>>, state: &mut Vec<usize>, i: usize) {
    if i == cc2.len() {
        res.push(state.clone());
        return;
    }
    let cc = &cc2[i];
    let l = cc[cc.len() - 1].1;

    for s in 0..(n - l) {
        let mut ok = true;
        for &(_, v) in cc {
            if state[s + v] != NONE {
                ok = false;
                break;
            }
        }

        if !ok {
            continue;
        }

        for &(k, v) in cc {
            state[s + v] = k;
        }

        dfs(n, res, cc2, state, i + 1);

        for &(_, v) in cc {
            state[s + v] = NONE;
        }
    }
}

fn main() {
    let (n, m) = read_uu();

    let mut puf = pot_union_find::PotUnionFind::new(n);

    for _ in 0..m {
        let (a, b, c) = read_uui();
        puf.union(a - 1, b - 1, c);
    }

    let mut components = puf.components();
    // println!("{components:?}");

    let mut cc2 = vec![];
    let mut c1 = vec![];
    for cc in components.iter_mut() {
        cc.sort_by_key(|v| v.1);
        let v0 = cc[0].1;

        let mut c2 = vec![];
        for &(k, v) in cc.iter() {
            c2.push((k, (v - v0) as usize));
        }

        if cc.len() == 1 {
            c1.push(cc[0].0);
        } else {
            cc2.push(c2);
        }
    }

    // println!("{c1:?} {:?}", cc2);

    let mut res = vec![];
    let mut state = vec![NONE; n];
    dfs(n, &mut res, &cc2, &mut state, 0);

    // println!("{res:?}");

    let mut pos = vec![vec![]; NONE + 1];
    for rr in &res {
        for i in 0..n {
            pos[rr[i]].push(i);
        }
    }

    for i in 0..=NONE {
        pos[i].dedup();
    }

    // println!("{pos:?}");

    let mut aa = vec![];
    for i in 0..n {
        let ans = if pos[i].len() == 0 {
            if c1.len() == 1 {
                if pos[NONE].len() == 1 {
                    pos[NONE][0] as i64 + 1
                } else {
                    -1
                }
            } else {
                -1
            }
        } else {
            if pos[i].len() == 1 {
                pos[i][0] as i64 + 1
            } else {
                -1
            }
        };
        aa.push(ans.to_string());
    }

    println!("{}", aa.join(" "));
}
