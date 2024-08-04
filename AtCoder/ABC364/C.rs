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
    let (n, x, y) = read_iii();
    let mut aa = read_vec();
    let mut bb = read_vec();
    aa.sort();
    aa.reverse();
    bb.sort();
    bb.reverse();

    let mut ans = n;

    let mut s = 0;
    let mut c = 0;
    for &a in &aa {
        s += a;
        c += 1;
        if s > x {
            ans = std::cmp::min(c, ans);
            break;
        }
    }

    let mut s = 0;
    let mut c = 0;
    for &a in &bb {
        s += a;
        c += 1;
        if s > y {
            ans = std::cmp::min(c, ans);
            break;
        }
    }

    println!("{ans}");
}
