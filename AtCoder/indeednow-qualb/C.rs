use std::io;
use std::collections::BinaryHeap;
use std::cmp::Reverse;

fn main() {
    let mut n = String::new();
    io::stdin().read_line(&mut n).unwrap();
    let n: i64 = n.trim().parse().unwrap();

    let mut edges: Vec<Vec<usize>> = Vec::new();
    let mut visited: Vec<bool> = Vec::new();

    for _ in 0..n {
        edges.push(Vec::new());
        visited.push(false);
    }

    for _ in 0..n-1 {
        let mut ab = String::new();
        io::stdin().read_line(&mut ab).unwrap();
        let ab: Vec<&str> = ab.split_whitespace().collect();
        let a: usize = ab[0].parse().unwrap();
        let b: usize = ab[1].parse().unwrap();

        edges[a-1].push(b-1);
        edges[b-1].push(a-1);

        //println!("{} {:?}  {} {}", i, ab, a, b);

    }

    //println!("{} {:?}", n, edges);

    let mut heap: BinaryHeap<Reverse<usize>> = BinaryHeap::new();
    heap.push(Reverse(0));

    let mut ans = String::new();

    while !heap.is_empty() {
        let p = if let Some(Reverse(v)) = heap.pop() { v } else { 0 };
        visited[p] = true;
        ans = ans + &format!("{} ", p+1)[..];
        //println!("{:?}", p);

        for e in &edges[p] {
            if !visited[*e] { heap.push(Reverse(*e)); }
        }
    }

    println!("{}", ans.trim());
}
