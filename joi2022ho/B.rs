fn main() {
    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();
    let nm: Vec<usize> = inp
        .trim()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect();
    // let n = nm[0];
    let m = nm[1];

    inp.clear();
    std::io::stdin().read_line(&mut inp).unwrap();
    let avec: Vec<usize> = inp
        .trim()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect();

    inp.clear();
    std::io::stdin().read_line(&mut inp).unwrap();
    let bvec: Vec<usize> = inp
        .trim()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect();

    // println!("{:?}", (n, m));
    // println!("{:?}", avec);
    // println!("{:?}", bvec);

    let cvec: Vec<_> = avec
        .iter()
        .zip(bvec.iter())
        .map(|(a, b)| std::cmp::max(a, b) * m)
        .collect();
    // println!("{:?}", cvec);

    let mut ok = 0;
    let mut ng = usize::MAX / 2;

    while ng - ok > 1 {
        let tgt = (ng + ok) / 2;
        if is_possible(tgt, &avec, &bvec, &cvec) {
            ok = tgt;
        } else {
            ng = tgt;
        }
    }

    println!("{}", ok);
}

fn is_possible(x: usize, avec: &Vec<usize>, bvec: &Vec<usize>, cvec: &Vec<usize>) -> bool {
    let mut free = 0;
    let mut need = 0;

    for (&a, (&b, &c)) in avec.iter().zip(bvec.iter().zip(cvec.iter())) {
        if c < x {
            need += (x - c + b - 1) / b;
        } else {
            free += (c - x) / std::cmp::max(a, b);
        }
    }

    free >= need
}
