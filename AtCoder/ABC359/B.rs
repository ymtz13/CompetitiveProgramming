fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i128> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (i128, i128) {
    let v = read_vec();
    (v[0], v[1])
}

fn main() {
    let (mut sx, mut sy) = read_uu();
    let (mut tx, mut ty) = read_uu();

    if sy % 2 == 0 {
        sx -= sx % 2;
    } else {
        sx -= (sx + 1) % 2;
    }

    if ty % 2 == 0 {
        tx -= tx % 2;
    } else {
        tx -= (tx + 1) % 2;
    }

    if sy > ty {
        (sx, tx) = (tx, sx);
        (sy, ty) = (ty, sy);
    }

    let dy = ty - sy;
    let mut ans = dy;

    if sx - dy > tx {
        ans += (sx - dy - tx) / 2;
    }
    if sx + dy < tx {
        ans += (tx - sx + dy) / 2;
    }

    println!("{ans}");
}
