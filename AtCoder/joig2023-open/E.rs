fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("");
    input
}

fn read_int_list() -> Vec<usize> {
    input()
        .split_whitespace()
        .map(|c| c.parse().expect(""))
        .collect()
}

fn pprint_matrix(matrix: &Vec<Vec<usize>>) {
    for row in matrix.iter() {
        for elm in row.iter() {
            print!("  {}", elm);
        }
        println!();
    }
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
    let hw = read_int_list();
    let h = hw[0];
    let w = hw[1];
    let n = h * w;

    let mut board = Vec::<Vec<usize>>::new();
    for _ in 0..h {
        board.push(read_int_list());
    }

    let mut uf_l = UnionFind::new(&n);
    let mut uf_r = UnionFind::new(&n);

    let mut map_l = vec![vec![0; w]; h];
    let mut map_r = vec![vec![0; w]; h];

    for iw_l in 0..w {
        let iw_r = w - 1 - iw_l;

        if iw_l > 0 {
            for ih in 0..h {
                let i_l = ih * w + iw_l;
                let i_r = ih * w + iw_r;

                if board[ih][iw_l] == board[ih][iw_l - 1] {
                    uf_l.union(&(i_l - 1), &i_l);
                }
                if board[ih][iw_r] == board[ih][iw_r + 1] {
                    uf_r.union(&(i_r + 1), &i_r);
                }
            }
        }

        for ih in 0..h - 1 {
            let i_l = ih * w + iw_l;
            let i_r = ih * w + iw_r;
            if board[ih][iw_l] == board[ih + 1][iw_l] {
                uf_l.union(&i_l, &(i_l + w));
            }
            if board[ih][iw_r] == board[ih + 1][iw_r] {
                uf_r.union(&i_r, &(i_r + w));
            }
        }

        for ih in 0..h {
            let i_l = ih * w + iw_l;
            let i_r = ih * w + iw_r;
            map_l[ih][iw_l] = uf_l.find(&i_l);
            map_r[ih][iw_r] = uf_r.find(&i_r);
        }
    }

    // pprint_matrix(&map_l);
    // pprint_matrix(&map_r);

    let mut ans = n;

    for k in 0..w - 1 {
        let mut a = uf_l.n;
        let mut hashset = std::collections::HashSet::new();

        for ih in 0..h {
            let vl = board[ih][k];
            let vr = board[ih][k + 1];

            if vl == vr {
                let t = (map_l[ih][k], map_r[ih][k + 1]);

                if !hashset.contains(&t) {
                    hashset.insert(t);
                    a += 1;
                }
                // println!("match! {k} {ih} {t:?}");
            }
        }

        // println!("{k} {a} {hashset:#?}");

        // println!("{k} {a}");

        ans = std::cmp::min(ans, a);
    }

    // println!("{:#?}", board);
    // println!("{:#?}", uf);

    println!("{}", ans);
}
