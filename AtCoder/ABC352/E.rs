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

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn main() {
    let nm = read_vec();
    let n = nm[0];
    let m = nm[1];

    let mut vv = vec![];
    for _ in 0..m {
        let kc = read_vec();
        let c = kc[1];
        let aa = read_vec();

        vv.push((c, aa));
    }
    vv.sort();

    let mut uf = UnionFind::new(n + 1);
    let mut ans = 0;

    for (c, aa) in &vv {
        let a0 = aa[0];
        for i in 1..aa.len() {
            let a = aa[i];
            if uf.find(a0) != uf.find(a) {
                uf.union(a0, a);
                ans += c;
            }
        }
    }

    println!("{}", if uf.n == 2 { ans as i64 } else { -1 });
}
