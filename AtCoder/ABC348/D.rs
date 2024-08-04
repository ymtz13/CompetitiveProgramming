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

static NULL: usize = 1000;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn bfs(aaa: &Vec<Vec<u8>>, bbb: &Vec<Vec<usize>>, s: (usize, usize), e: usize, h: usize, w: usize) -> Vec<usize> {
    let mut ret = vec![];
    let mut queue = std::collections::VecDeque::new();
    queue.push_front((s, e));
    let mut visited = std::collections::HashSet::new();

    while let Some(((r, c), e)) = queue.pop_back() {
        if visited.contains(&(r, c)) {
            continue;
        }
        visited.insert((r, c));

        if bbb[r][c] != NULL {
            ret.push(bbb[r][c]);
        }

        if e == 0 {
            continue;
        }

        if 0 < r {
            queue.push_front(((r - 1, c), e));
        }
        if r < h - 1 {
            queue.push_front(((r + 1, c), e));
        }
        if 0 < c {
            queue.push_front(((r, c - 1), e));
        }
        if c < w - 1 {
            queue.push_front(((r, c + 1), e));
        }
    }

    ret
}

fn main() {
    let hw = read_vec();
    let h = hw[0] as usize;
    let w = hw[1] as usize;

    let mut aaa = vec![];
    for _ in 0..h {
        let aa: Vec<_> = read_line().bytes().collect();
        aaa.push(aa);
    }

    let n: usize = read_line().parse().unwrap();
    let mut pp = vec![];
    let mut bbb = vec![vec![NULL; w]; h];
    for i in 1..=n {
        let rce = read_vec();
        let r = rce[0] as usize;
        let c = rce[1] as usize;
        let e = rce[2];
        pp.push((r, c, e));
        bbb[r][c] = i;
    }

    for aa in &aaa {
        println!("{:?}", aa);
    }
    for bb in &bbb {
        println!("{:?}", bb);
    }
}
