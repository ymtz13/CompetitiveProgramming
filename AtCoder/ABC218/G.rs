fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

use std::collections::{BinaryHeap, HashMap};

struct DeletableHeap {
    heap: BinaryHeap<i64>,
    len: usize,
    deleted: HashMap<i64, usize>,
}

impl DeletableHeap {
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

    fn push(&mut self, value: i64) {
        self.heap.push(value);
        self.len += 1;
    }

    fn pop(&mut self) -> Option<i64> {
        self.peek();
        self.len -= 1;
        self.heap.pop()
    }

    fn delete(&mut self, value: i64) {
        self.len -= 1;
        self.deleted.entry(value).and_modify(|cnt| *cnt += 1).or_insert(1);
    }

    fn peek(&mut self) -> Option<i64> {
        loop {
            let v = self.heap.peek();
            if v.is_none() {
                return None;
            }
            let v = v.unwrap().clone();

            if self.deleted.get(&v).is_some_and(|cnt| *cnt > 0) {
                self.deleted.entry(v).and_modify(|cnt| *cnt -= 1);
                self.heap.pop();
            } else {
                return Some(v);
            }
        }
    }
}

struct MedianSet {
    l_heap: DeletableHeap,
    r_heap: DeletableHeap,
}

impl MedianSet {
    fn new() -> Self {
        Self {
            l_heap: DeletableHeap::new(),
            r_heap: DeletableHeap::new(),
        }
    }

    fn push(&mut self, value: i64) {
        if self.l_heap.peek().is_some_and(|v| value <= v) {
            self.l_heap.push(value);
        } else {
            self.r_heap.push(-value);
        }

        self.normalize();
    }

    fn delete(&mut self, value: i64) {
        if self.l_heap.peek().is_some_and(|v| value <= v) {
            self.l_heap.delete(value);
        } else {
            self.r_heap.delete(-value);
        }

        self.normalize();
    }

    fn normalize(&mut self) {
        let l_heap = &mut self.l_heap;
        let r_heap = &mut self.r_heap;

        while l_heap.len() > r_heap.len() + 1 {
            let v = l_heap.pop().unwrap();
            r_heap.push(-v);
        }

        while l_heap.len() < r_heap.len() {
            let v = r_heap.pop().unwrap();
            l_heap.push(-v);
        }
    }

    fn median(&mut self) -> i64 {
        if self.l_heap.len() == self.r_heap.len() {
            let lv = self.l_heap.peek().unwrap();
            let rv = self.r_heap.peek().unwrap();
            (lv - rv) / 2
        } else {
            self.l_heap.peek().unwrap()
        }
    }
}

fn calc_leaf_scores(childs: &Vec<Vec<usize>>, aa: &Vec<i64>, ms: &mut MedianSet, scores: &mut Vec<i64>, i: usize) {
    let a = aa[i];
    ms.push(a);

    if childs[i].len() == 0 {
        scores[i] = ms.median();
    } else {
        for &j in &childs[i] {
            calc_leaf_scores(childs, aa, ms, scores, j);
        }
    }

    ms.delete(a);
}

fn solve(childs: &Vec<Vec<usize>>, scores: &Vec<i64>, i: usize, depth: usize) -> i64 {
    if childs[i].len() == 0 {
        return scores[i];
    }

    let mut ss = vec![];
    for &j in &childs[i] {
        ss.push(solve(childs, scores, j, depth + 1));
    }

    if depth % 2 == 0 {
        scores[i] + ss.iter().max().unwrap()
    } else {
        scores[i] + ss.iter().min().unwrap()
    }
}

fn main() {
    let n: usize = read_line().parse().unwrap();

    let mut aa = vec![0];
    aa.extend(read_vec());
    let aa = aa;

    let mut edges = vec![vec![]; n + 1];
    for _ in 0..n - 1 {
        let uv = read_vec();
        let u = uv[0] as usize;
        let v = uv[1] as usize;

        edges[u].push(v);
        edges[v].push(u);
    }

    use std::collections::VecDeque;
    let mut queue = VecDeque::from(vec![(1, 0)]);
    let mut visited = vec![false; n + 1];
    let mut childs = vec![vec![]; n + 1];
    while let Some((i, d)) = queue.pop_back() {
        visited[i] = true;

        for &j in &edges[i] {
            if visited[j] {
                continue;
            }
            queue.push_front((j, d + 1));
            childs[i].push(j);
        }
    }

    let mut scores = vec![0; n + 1];
    let mut ms = MedianSet::new();
    calc_leaf_scores(&childs, &aa, &mut ms, &mut scores, 1);

    let ans = solve(&childs, &scores, 1, 0);
    println!("{ans:?}");
}
