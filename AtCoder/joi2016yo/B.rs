fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    let nm = input();
    let nm: Vec<usize> = nm.split_whitespace().map(|c| c.parse().unwrap()).collect();
    let n = nm[0];
    let m = nm[1];

    let mut alist = Vec::new();
    for _ in 0..n {
        let a: usize = input().trim().parse().unwrap();
        alist.push(a);
    }

    for k in 1..=m {
        for i in 0..n - 1 {
            let j = i + 1;
            let ai = alist[i];
            let aj = alist[j];
            if ai % k > aj % k {
                alist[i] = aj;
                alist[j] = ai;
            }
        }
    }

    for a in &alist {
        println!("{}", a);
    }
}
