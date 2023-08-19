fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn read_int_vec() -> Vec<usize> {
    input()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect()
}

fn main() {
    let nmd = read_int_vec();
    let n = nmd[0];
    let m = nmd[1];
    let d = nmd[2];

    let mut xvs = Vec::<(usize, usize)>::new();
    for _ in 0..n {
        let xv = read_int_vec();
        xvs.push((xv[0], xv[1]));
    }
    xvs.sort();

    let mut dp = Vec::<(usize, usize)>::new();
    dp.push((0, 0));
    let mut i: usize = 0;

    println!("{xvs:?}");
}
