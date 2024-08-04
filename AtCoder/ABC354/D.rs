use std::cmp::max;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let abcd = read_line();
    let mut abcd = abcd.split_whitespace();
    let x_l: i64 = abcd.next().unwrap().parse::<i64>().unwrap() + 1_000_000_000;
    let y_b: i64 = abcd.next().unwrap().parse::<i64>().unwrap() + 1_000_000_000;
    let x_r: i64 = abcd.next().unwrap().parse::<i64>().unwrap() + 1_000_000_000;
    let y_u: i64 = abcd.next().unwrap().parse::<i64>().unwrap() + 1_000_000_000;

    let x_lz = (x_l + 3) / 4 * 4;
    let x_rz = x_r / 4 * 4;

    let ny = y_u - y_b;
    let ny0 = (y_u + 1) / 2 - (y_b + 1) / 2;
    let ny1 = ny - ny0;

    // println!("{:?}", (x_l, x_r, (x_lz, x_rz)));
    // println!("{:?}", (y_u, y_b, (ny, ny0, ny1)));

    let mut ans = max(x_rz - x_lz, 0) * ny;

    for x in (x_l..x_lz).chain(x_rz..x_r) {
        if x % 4 == 0 {
            ans += ny0 * 2 + ny1;
        }
        if x % 4 == 1 {
            ans += ny0 + ny1 * 2;
        }
        if x % 4 == 2 {
            ans += ny1;
        }
        if x % 4 == 3 {
            ans += ny0;
        }
    }

    println!("{ans}");
}
