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

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_uu() -> (usize, usize) {
    let vv: Vec<_> = read_line().split_whitespace().map(|v| v.parse().unwrap()).collect();
    (vv[0], vv[1])
}

fn main() {
    let (n, m) = read_uu();

    let mut uf = UnionFind::new(&n);

    for _ in 0..m {
        let (a, b) = read_uu();
        uf.union(&(a - 1), &(b - 1));
    }

    for i in 0..n {
        uf.find(&i);
    }

    let mut ans = 0;

    for i in 0..n {
        if uf.find(&i) == i {
            let s = uf.size(&i);
            ans += s * (s - 1) / 2;
        }
    }

    ans -= m;

    println!("{ans}");
}
