use std::collections::{BinaryHeap, HashMap};

struct DeletableHeap<T> {
    heap: BinaryHeap<T>,
    len: usize,
    deleted: HashMap<T, usize>,
}

impl<T: std::cmp::Ord + std::hash::Hash> DeletableHeap<T> {
    fn new() -> Self {
        Self {
            heap: BinaryHeap::new(),
            len: 0,
            deleted: HashMap::new(),
        }
    }

    fn len(&self) -> usize {
        self.len
    }

    fn push(&mut self, value: T) {
        self.heap.push(value);
        self.len += 1;
    }

    fn pop(&mut self) -> Option<T> {
        self.len -= 1;
        let res = self.heap.pop();
        self.cleanup();

        res
    }

    fn delete(&mut self, value: T) {
        self.len -= 1;
        self.deleted.entry(value).and_modify(|cnt| *cnt += 1).or_insert(1);
        self.cleanup();
    }

    fn cleanup(&mut self) {
        while let Some(v) = self.heap.peek() {
            if let Some(cnt) = self.deleted.get_mut(&v) {
                if *cnt == 0 {
                    return;
                }
                *cnt -= 1;
                self.heap.pop();
                continue;
            }
            return;
        }
    }

    fn peek(&self) -> Option<&T> {
        self.heap.peek()
    }
}

fn main() {
    let mut heap = DeletableHeap::new();
    heap.push(1);
    heap.push(2);
    heap.push(3);

    heap.delete(3);

    assert_eq!(heap.pop(), Some(2));
    assert_eq!(heap.peek(), Some(&1));
    assert_eq!(heap.len(), 1);

    heap.push(3);
    assert_eq!(heap.peek(), Some(&3));
    assert_eq!(heap.len(), 2);
}

// struct MedianSet {
//     l_heap: DeletableHeap,
//     r_heap: DeletableHeap,
// }

// impl MedianSet {
//     fn new() -> Self {
//         Self {
//             l_heap: DeletableHeap::new(),
//             r_heap: DeletableHeap::new(),
//         }
//     }

//     fn push(&mut self, value: i64) {
//         if self.l_heap.peek().is_some_and(|v| value <= v) {
//             self.l_heap.push(value);
//         } else {
//             self.r_heap.push(-value);
//         }

//         self.normalize();
//     }

//     fn delete(&mut self, value: i64) {
//         if self.l_heap.peek().is_some_and(|v| value <= v) {
//             self.l_heap.delete(value);
//         } else {
//             self.r_heap.delete(-value);
//         }

//         self.normalize();
//     }

//     fn normalize(&mut self) {
//         let l_heap = &mut self.l_heap;
//         let r_heap = &mut self.r_heap;

//         while l_heap.len() > r_heap.len() + 1 {
//             let v = l_heap.pop().unwrap();
//             r_heap.push(-v);
//         }

//         while l_heap.len() < r_heap.len() {
//             let v = r_heap.pop().unwrap();
//             l_heap.push(-v);
//         }
//     }

//     fn median(&mut self) -> i64 {
//         if self.l_heap.len() == self.r_heap.len() {
//             let lv = self.l_heap.peek().unwrap();
//             let rv = self.r_heap.peek().unwrap();
//             (lv - rv) / 2
//         } else {
//             self.l_heap.peek().unwrap()
//         }
//     }
// }
