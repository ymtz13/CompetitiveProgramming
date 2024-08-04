fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i128> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let aa = read_vec();

    let mut dd = vec![1; n];
    let mut heap = std::collections::BinaryHeap::new();
    for i in 0..n {
        let a = aa[i];
        heap.push((-3 * a, i));
    }

    for _ in 0..n - 2 {
        let (_, i) = heap.pop().unwrap();
        dd[i] += 1;
        heap.push((-(2 * dd[i] + 1) * aa[i], i));
    }

    let mut ans = 0;
    for i in 0..n {
        ans += dd[i] * dd[i] * aa[i];
    }

    println!("{ans}");
}
