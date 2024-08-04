fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

type Int = usize;

fn read_vec() -> Vec<Int> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_ii() -> (Int, Int) {
    let v = read_vec();
    (v[0], v[1])
}

fn read_iii() -> (Int, Int, Int) {
    let v = read_vec();
    (v[0], v[1], v[2])
}

fn main() {
    let (h, w) = read_ii();
    let (mut si, mut sj) = read_ii();
    si -= 1;
    sj -= 1;

    let mut ccc: Vec<_> = (0..h).map(|_| read_line().into_bytes()).collect();

    let xx = read_line().into_bytes();

    for &x in &xx {
        if x == b'L' && sj > 0 && ccc[si][sj - 1] != b'#' {
            sj -= 1;
        }
        if x == b'R' && sj < w - 1 && ccc[si][sj + 1] != b'#' {
            sj += 1;
        }
        if x == b'U' && si > 0 && ccc[si - 1][sj] != b'#' {
            si -= 1;
        }
        if x == b'D' && si < h - 1 && ccc[si + 1][sj] != b'#' {
            si += 1;
        }
    }

    println!("{} {}", si + 1, sj + 1);
}
