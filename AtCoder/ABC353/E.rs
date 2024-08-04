use std::collections::VecDeque;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<String> {
    read_line().split_whitespace().map(|s| String::from(s)).collect()
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let ss0 = read_vec();

    let mut ss = vec![];
    for s in &ss0 {
        let bytes: Vec<_> = s.bytes().map(|b| b - b'a').collect();
        ss.push(VecDeque::from(bytes));
    }

    let mut ans = 0;

    // println!("{ss:?}");

    let mut queue = VecDeque::from(vec![ss]);
    while let Some(ss) = queue.pop_front() {
        let mut backets = vec![vec![]; 26];

        for mut s in ss {
            let first = s.pop_front();
            if let Some(first) = first {
                backets[first as usize].push(s);
            }
        }

        for backet in backets.into_iter() {
            let l = backet.len();
            if l > 0 {
                // println!("{backet:?}");
                ans += l * (l - 1) / 2;
                queue.push_back(backet);
            }
        }
    }

    println!("{ans}");
}
