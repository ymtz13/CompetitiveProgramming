fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let n: usize = read_line().parse().unwrap();

    let mut aaa = vec![];
    let mut bbb = vec![];
    for _ in 0..n {
        aaa.push(read_line().into_bytes());
    }
    for _ in 0..n {
        bbb.push(read_line().into_bytes());
    }

    for i in 0..n {
        for j in 0..n {
            if aaa[i][j] != bbb[i][j] {
                println!("{} {}", i + 1, j + 1);
            }
        }
    }
}
