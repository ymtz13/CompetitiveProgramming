use std::collections::{BinaryHeap, HashMap};
use std::iter::FromIterator;

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    let nq = input();
    let mut nq = nq.split_whitespace().map(|c| c.parse().unwrap());
    let n: usize = nq.next().unwrap();
    let q: usize = nq.next().unwrap();

    let mut heap = BinaryHeap::new();
    for a in 0..n + 1 {
        for b in 0..n - a + 1 {
            let c = n - a - b;
            heap.push((0, "A".repeat(a) + &"B".repeat(b) + &"C".repeat(c)));
        }
    }

    // println!("{:?}", heap);

    let mut cnt = HashMap::new();

    while heap.len() > 0 {
        let (c, s) = match heap.pop() {
            Some(v) => v,
            None => break,
        };

        if let Some(_) = cnt.get(&s) {
            continue;
        }

        cnt.insert(s.clone(), -c);

        for i in 2..n + 1 {
            let front = String::from(&s[0..i]);
            let back = &s[i..];

            let ss = String::from_iter(front.chars().rev()) + back;
            heap.push((c - 1, ss));
        }
    }

    // println!("{:?}", cnt);

    for _ in 0..q {
        let s = input();
        let s = s.trim();
        println!("{}", cnt.get(s).unwrap());
    }
}
