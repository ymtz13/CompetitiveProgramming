fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_ii() -> (i64, i64) {
    let a = read_vec();
    (a[0], a[1])
}

fn f(x: i64, y: i64, k: i64) -> Vec<(i64, i64, i64)> {
    let dx = x / k;
    let dy = y / k;
    let d = (dx + dy) % 2;

    if d == 1 {
        return vec![(dx, dy, 0)];
    }

    let rx = x % k;
    let ry = y % k;

    vec![(dx - 1, dy, rx + 1), (dx + 1, dy, k - rx), (dx, dy - 1, ry + 1), (dx, dy + 1, k - ry)]
}

fn main() {
    let k: i64 = read_line().parse().unwrap();
    let (sx, sy) = read_ii();
    let (tx, ty) = read_ii();

    if k == 1 {
        println!("{}", (sx - tx).abs() + (sy - ty).abs());
        return;
    }

    let sx = sx + k * 2;
    let sy = sy + k * 2;
    let tx = tx + k * 2;
    let ty = ty + k * 2;

    let dsx = sx / k;
    let dsy = sy / k;
    let dtx = tx / k;
    let dty = ty / k;

    let mut ans = i64::MAX >> 1;

    if dsx == dtx && dsy == dty {
        if (dsx + dsy) % 2 == 1 {
            println!("0");
            return;
        }
        ans = (sx - tx).abs() + (sy - ty).abs();
    }

    let fs = f(sx, sy, k);
    let ft = f(tx, ty, k);

    // println!("ans: {ans}");
    // println!("fs: {fs:?}");
    // println!("ft: {ft:?}");

    for &(dsx, dsy, cs) in &fs {
        let ps = (dsx + dsy + 1) / 2;
        let qs = (dsx - dsy + 1) / 2;

        for &(dtx, dty, ct) in &ft {
            let pt = (dtx + dty + 1) / 2;
            let qt = (dtx - dty + 1) / 2;

            let mut dp = (ps - pt).abs();
            let mut dq = (qs - qt).abs();

            if dp > dq {
                (dp, dq) = (dq, dp);
            }

            let c = if k >= 3 { (dp + dq) * 2 } else { dp * 3 + (dq - dp) * 2 };
            let cost = c + cs + ct;

            // println!("{:?} {:?} {:?}", (dsx, dsy, cs), (dtx, dty, ct), ((ps, qs), (pt, qt), c));

            ans = std::cmp::min(ans, cost);
        }
    }

    println!("{ans}");
}
