fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn main() {
    let nm = input();
    let mut nm = nm.split_whitespace().map(|c| c.parse().unwrap());
    let n: usize = nm.next().unwrap();
    let m: usize = nm.next().unwrap();

    let mut box_of = vec![0; n + 1];
    for i in 1..n + 1 {
        box_of[i] = i;
    }

    for _ in 0..m {
        let xy = input();
        let mut xy = xy.split_whitespace().map(|c| c.parse().unwrap());
        let x: usize = xy.next().unwrap();
        let y: usize = xy.next().unwrap();

        box_of[x] = y;
    }

    for i in 1..n + 1 {
        println!("{}", box_of[i]);
    }
}
