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

    let mut cnt = vec![-1; 3_usize.pow(n as u32)];

    fn to_index(s: &str) -> usize {
        let mut ret = 0;
        for (i, c) in s.chars().enumerate() {
            ret += 3_usize.pow(i as u32)
                * (match c {
                    'A' => 0,
                    'B' => 1,
                    _ => 2,
                })
        }
        ret
    }

    while heap.len() > 0 {
        let (c, s) = match heap.pop() {
            Some(v) => v,
            None => break,
        };

        let index = to_index(&s);

        if cnt[index] >= 0 {
            continue;
        }

        cnt[index] = -c;

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
        println!("{}", cnt[to_index(&s)]);
    }
}
