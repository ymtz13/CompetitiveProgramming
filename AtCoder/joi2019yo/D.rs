use std::collections::HashMap;

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    let n: usize = input().trim().parse().unwrap();
    let alist = input();
    let alist: Vec<i64> = alist
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect();

    let mut map = HashMap::new();
    for (i, a) in alist.iter().enumerate() {
        map.entry(a).or_insert(vec![]).push(i + 1);
    }

    if let Some(vec) = map.get(&0) {
        if vec.len() == n {
            println!("0");
            return;
        }
    }

    // println!("{:?}", map);

    let mut map: Vec<_> = map.iter().collect();
    map.sort_by_key(|e| e.0);
    // println!("{:?}", map);

    let mut is_land = vec![1; n + 2];
    is_land[0] = 0;
    is_land[n + 1] = 0;

    let mut current = 1;
    let mut ans = 1;
    for (_, vec) in map {
        for v in vec {
            is_land[*v] = 0;
            current += is_land[v - 1] + is_land[v + 1] - 1;
            // println!("v={}, current={}, ans={}", v, current, ans);
        }
        ans = std::cmp::max(ans, current);
    }

    println!("{}", ans);
}
