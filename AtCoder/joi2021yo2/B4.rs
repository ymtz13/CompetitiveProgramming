use std::collections::BinaryHeap;

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn to_index(s: &[usize], pow3: &[usize]) -> usize {
    let mut ret = 0;
    for (c, p) in s.iter().zip(pow3.iter()) {
        ret += c * p;
    }
    ret
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
            let mut vec = vec![0; a];
            vec.append(&mut vec![1; b]);
            vec.append(&mut vec![2; c]);
            heap.push((0, vec));
        }
    }

    // println!("{:?}", heap);

    let mut cnt = vec![-1; 3_usize.pow(n as u32)];

    let pow3: Vec<_> = (0..n).map(|v| 3_usize.pow(v as u32)).collect();

    while let Some((c, s)) = heap.pop() {
        let index = to_index(&s, &pow3);

        if cnt[index] >= 0 {
            continue;
        }

        cnt[index] = -c;

        for i in 2..=n {
            let mut ss = s.clone();
            // let mut back = ss.split_off(i);

            // ss.reverse();
            // ss.append(&mut back);
            for l in 0..i / 2 {
                let r = i - l - 1;
                let tmp = ss[l];
                ss[l] = ss[r];
                ss[r] = tmp;
            }

            heap.push((c - 1, ss));
        }
    }

    // println!("{:?}", cnt);

    for _ in 0..q {
        let s = input();
        let s = s.trim();

        let mut index = 0;
        for (i, c) in s.chars().enumerate() {
            index += 3_usize.pow(i as u32)
                * match c {
                    'A' => 0,
                    'B' => 1,
                    _ => 2,
                };
        }

        println!("{}", cnt[index]);
    }
}
