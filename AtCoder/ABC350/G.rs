const MOD: usize = 998244353;

#[derive(Debug, Clone, Copy)]
enum Node {
    Root(usize),
    ChildOf(usize),
}

#[derive(Debug)]
struct UnionFind {
    nodes: Vec<Node>,
    n: usize,
}

impl UnionFind {
    fn new(length: usize) -> UnionFind {
        UnionFind {
            nodes: vec![Node::Root(1); length],
            n: length,
        }
    }

    fn find(&mut self, index: usize) -> usize {
        match self.nodes[index] {
            Node::Root(_) => index,
            Node::ChildOf(parent_index) => {
                let root_index = self.find(parent_index);
                self.nodes[index] = Node::ChildOf(root_index);
                root_index
            }
        }
    }

    fn size(&mut self, index: usize) -> usize {
        let root_index = self.find(index);
        match self.nodes[root_index] {
            Node::Root(size) => size,
            _ => panic!(),
        }
    }

    fn union(&mut self, index1: usize, index2: usize) {
        let mut root_index1 = self.find(index1);
        let mut root_index2 = self.find(index2);
        if root_index1 == root_index2 {
            return;
        }

        let size1 = self.size(root_index1);
        let size2 = self.size(root_index2);

        if size1 < size2 {
            let temp = root_index1;
            root_index1 = root_index2;
            root_index2 = temp;
        }

        self.nodes[root_index1] = Node::Root(size1 + size2);
        self.nodes[root_index2] = Node::ChildOf(root_index1);
        self.n -= 1;
    }
}

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_uu() -> (usize, usize) {
    let vv: Vec<_> = read_line().split_whitespace().map(|v| v.parse().unwrap()).collect();
    (vv[0], vv[1])
}

fn read_uuu() -> (usize, usize, usize) {
    let vv: Vec<_> = read_line().split_whitespace().map(|v| v.parse().unwrap()).collect();
    (vv[0], vv[1], vv[2])
}

use std::collections::VecDeque;

fn main() {
    let (n, q) = read_uu();
    let mut x = 0;

    let mut parent = vec![0; n + 1];
    let mut depth = vec![0i64; n + 1];
    let mut ee = vec![vec![]; n + 1];
    let mut uf = UnionFind::new(n + 1);

    let mut ans = vec![];

    for _ in 0..q {
        let (a, b, c) = read_uuu();
        let t = 1 + (a * (1 + x)) % MOD % 2;
        let u = 1 + (b * (1 + x)) % MOD % n;
        let v = 1 + (c * (1 + x)) % MOD % n;

        if t == 1 {
            ee[u].push(v);
            ee[v].push(u);

            let u0 = uf.find(u);

            uf.union(u, v);

            let mut queue = VecDeque::from(vec![if uf.find(u) == u0 { (v, depth[u] + 1, u) } else { (u, depth[v] + 1, v) }]);

            while let Some((q, d, p)) = queue.pop_front() {
                parent[q] = p;
                depth[q] = d;

                for &e in &ee[q] {
                    if e != p {
                        queue.push_back((e, d + 1, q));
                    }
                }
            }
        } else {
            let du = depth[u];
            let dv = depth[v];

            if du == dv {
                x = if parent[u] == parent[v] { parent[u] } else { 0 };
            } else if du - dv == 2 {
                x = if parent[parent[u]] == v { parent[u] } else { 0 };
            } else if dv - du == 2 {
                x = if parent[parent[v]] == u { parent[v] } else { 0 };
            } else {
                x = 0;
            }

            ans.push(x);
        }
    }

    ans.iter().for_each(|x| println!("{x}"));
}
