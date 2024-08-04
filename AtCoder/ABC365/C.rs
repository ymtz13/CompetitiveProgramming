fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let nm = read_vec();
    let n = nm[0];
    let m = nm[1];

    let aa = read_vec();

    let mut ok = 0;
    let mut ng = 1 << 30;

    while ng - ok > 1 {
        let x = (ng + ok) / 2;

        let mut s = 0;
        for &a in &aa {
            s += std::cmp::min(a, x);
        }

        if s <= m {
            ok = x;
        } else {
            ng = x;
        }
    }

    if ok == (1 << 30) - 1 {
        println!("infinite");
    } else {
        println!("{ok}");
    }
}
