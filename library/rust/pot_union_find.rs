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

fn main() {
    let mut puf = pot_union_find::PotUnionFind::new(10);
    println!("{:?}", puf.components());

    puf.union(3, 5, 100);
    puf.union(6, 7, 200);
    puf.union(5, 1, -300);
    println!("{:?}", puf.components());
}
