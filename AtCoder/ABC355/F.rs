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
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (usize, usize) {
    let uu = read_vec();
    (uu[0], uu[1])
}

fn read_uuu() -> (usize, usize, usize) {
    let uu = read_vec();
    (uu[0], uu[1], uu[2])
}

fn main() {
    let (n, q) = read_uu();

    // ufs[d]: コストd以下の辺だけ含む
    let mut ufs: Vec<_> = (0..=10).map(|_| UnionFind::new(n + 1)).collect();
    let mut z = 0;

    let mut uf = UnionFind::new(n + 1);

    for _ in 0..n - 1 {
        let (a, b, c) = read_uuu();
        for d in 1..=10 {
            if c <= d {
                ufs[d].union(a, b);
            }
        }

        if uf.find(a) != uf.find(b) {
            z += c;
            uf.union(a, b);
        }
    }

    for _ in 0..q {
        let (a, b, c) = read_uuu();

        let mut d = 1;
        while d <= 10 {
            let uf = &mut ufs[d];
            if uf.find(a) == uf.find(b) {
                break;
            }
            d += 1;
        }

        if c < d {
            z += c;
            z -= d;
        }

        for d in 1..=10 {
            if c <= d {
                ufs[d].union(a, b);
            }
        }

        println!("{z}");
    }
}
