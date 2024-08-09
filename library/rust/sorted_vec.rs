#[derive(Debug)]
struct InternalNode<T> {
    value: T,
    lchild: usize,
    rchild: usize,
}

struct SortedVec<T> {
    vec: Vec<Option<InternalNode<T>>>,
    iroot: usize,
}

impl<T: std::cmp::PartialOrd> SortedVec<T> {
    fn new() -> SortedVec<T> {
        SortedVec { vec: vec![None], iroot: 0 }
    }

    fn get(&self, index: usize) -> Option<&InternalNode<T>> {
        self.vec.get(index).and_then(|v| v.as_ref())
    }

    fn take(&mut self, index: usize) -> Option<InternalNode<T>> {
        self.vec.get_mut(index).and_then(|v| v.take())
    }

    fn contains(&self, value: &T) -> bool {
        let mut i = self.iroot;
        while let Some(node) = self.get(i) {
            if *value == node.value {
                return true;
            }

            if *value < node.value {
                i = node.lchild
            } else {
                i = node.rchild;
            };
        }

        false
    }

    fn insert(&mut self, value: T) {
        let mut i = self.iroot;
        while let Some(node) = self.get(i) {
            if value < node.value {
                i = node.lchild;
            } else {
                i = node.rchild;
            }
        }

        let lchild = self.vec.len();
        let rchild = lchild + 1;

        self.vec.push(None);
        self.vec.push(None);

        self.vec.get_mut(i).map(|v| *v = Some(InternalNode { value, lchild, rchild }));
    }

    fn remove(&mut self, value: &T) -> bool {
        let mut i = self.iroot;
        while let Some(node) = self.get(i) {
            if *value == node.value {
                break;
            }

            if *value < node.value {
                i = node.lchild;
            } else {
                i = node.rchild;
            }
        }

        let target = self.take(i);
        // let z: () = target;
        match target {
            None => return false,
            Some(node) => {
                let (lnode, rnode) = (self.get(node.lchild), self.get(node.rchild));
                match (lnode, rnode) {
                    (None, _) => {
                        let node = self.take(node.rchild);
                        self.vec.get_mut(i).map(|v| *v = node);
                    }
                    (Some(_), None) => {
                        let node = self.take(node.lchild);
                        self.vec.get_mut(i).map(|v| *v = node);
                    }
                    (Some(lnode), Some(_)) => {}
                }
            }
        }

        true
    }
}

fn main() {
    // let mut aa: Vec<_> = (0..5i32).map(|v| Some(v)).collect();
    // let z: () = aa.get_mut(2);

    // let x = aa.get_mut(2).map(|v| v.take());
    // println!("{x:?} {aa:?}");

    let mut sv = SortedVec::new();

    sv.insert(6);
    sv.insert(4);
    sv.insert(9);
    sv.insert(5);
    sv.insert(3);

    for i in 0..sv.vec.len() {
        println!("{i}:{:?}", sv.vec[i]);
    }
}
