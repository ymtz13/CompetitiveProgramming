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
    let v: Vec<_> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    (v[0], v[1])
}

fn main() {
    let (n, m) = read_uu();
    let mut edges = vec![];
    let mut dd = vec![0; n + 1];

    for _ in 0..m {
        let (a, b) = read_uu();
        edges.push((a, b));
        dd[a] += 1;
        dd[b] += 1;
    }

    let mut x6 = 0;
    let mut x4 = 0;
    let mut i4 = 0;
    for i in 1..=n {
        if dd[i] % 2 == 1 {
            println!("No");
            return;
        }
        if dd[i] >= 6 {
            x6 += 1;
        }
        if dd[i] == 4 {
            x4 += 1;
            i4 = i;
        }
    }

    if x6 >= 1 || x4 >= 3 {
        println!("Yes");
        return;
    }
    if x4 == 2 {
        let mut uf = UnionFind::new(n + 1);
        for &(a, b) in &edges {
            if a != i4 && b != i4 {
                uf.union(a, b);
            }
        }
        if uf.n >= 4 {
            println!("Yes");
            return;
        }
    }

    println!("No");
}
