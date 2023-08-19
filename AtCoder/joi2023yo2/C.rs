use std::collections::HashMap;
use std::collections::HashSet;
use std::convert::TryInto;

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("");
    input
}

fn read_int_vec() -> Vec<usize> {
    input()
        .split_whitespace()
        .map(|c| c.parse().expect(""))
        .collect()
}

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
    fn new(length: &usize) -> UnionFind {
        let mut nodes = Vec::new();
        for _ in 0..*length {
            nodes.push(Node::Root(1));
        }
        UnionFind { nodes, n: *length }
    }

    fn find(&mut self, index: &usize) -> usize {
        let node = self.nodes[*index];
        match node {
            Node::Root(_) => *index,
            Node::ChildOf(parent_index) => {
                let root_index = self.find(&parent_index);
                self.nodes[*index] = Node::ChildOf(root_index);
                root_index
            }
        }
    }

    fn size(&mut self, index: &usize) -> usize {
        let root_index = self.find(index);
        match self.nodes[root_index] {
            Node::Root(size) => size,
            _ => panic!(),
        }
    }

    fn union(&mut self, index1: &usize, index2: &usize) {
        let mut root_index1 = self.find(index1);
        let mut root_index2 = self.find(index2);
        if root_index1 == root_index2 {
            return;
        }

        let size1 = self.size(&root_index1);
        let size2 = self.size(&root_index2);

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

fn main() {
    let hw = read_int_vec();
    let h = hw[0];
    let w = hw[1];
    let n: usize = (h * w).try_into().unwrap();

    let mut a = Vec::<Vec<usize>>::new();

    for _ in 0..h {
        a.push(read_int_vec());
    }

    let mut uf = UnionFind::new(&n);

    for ih in 0..h {
        for iw in 0..w {
            let i = ih * w + iw;
            let ir = i + 1;
            let id = i + w;

            if iw < w - 1 && a[ih][iw] == a[ih][iw + 1] {
                uf.union(&i, &ir);
            }
            if ih < h - 1 && a[ih][iw] == a[ih + 1][iw] {
                uf.union(&i, &id);
            }
        }
    }

    let mut neighbors = Vec::<HashSet<usize>>::new();
    for _ in 0..n {
        neighbors.push(HashSet::new());
    }

    for ih in 0..h {
        for iw in 0..w {
            let i = ih * w + iw;
            let ir = i + 1;
            let id = i + w;

            if iw < w - 1 && a[ih][iw] != a[ih][iw + 1] {
                let index1 = uf.find(&i);
                let index2 = uf.find(&ir);
                neighbors[index1].insert(index2);
                neighbors[index2].insert(index1);
            }
            if ih < h - 1 && a[ih][iw] != a[ih + 1][iw] {
                let index1 = uf.find(&i);
                let index2 = uf.find(&id);
                neighbors[index1].insert(index2);
                neighbors[index2].insert(index1);
            }
        }
    }

    // println!("{:#?}", neighbors);

    let mut ans = 0;

    for (i, neighbor) in neighbors.iter().enumerate() {
        let mut counts = HashMap::<usize, usize>::new();
        let size_i = uf.size(&i);

        for j in neighbor {
            let c = a[j / w][j % w];
            let size_j = uf.size(&j);
            counts.entry(c).or_insert(0);
            counts.entry(c).and_modify(|v| *v += size_j);
        }

        ans = std::cmp::max(ans, size_i);
        for (_, count) in counts.iter() {
            ans = std::cmp::max(ans, size_i + count);
        }

        // println!("{} -> {:#?}", i, counts);
    }

    println!("{}", ans);
}
