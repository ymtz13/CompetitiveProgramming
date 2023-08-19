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
