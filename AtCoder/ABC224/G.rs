fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let v: Vec<f64> = read_line().split_whitespace().map(|c| c.parse().unwrap()).collect();
    let n = v[0];
    let s = v[1];
    let t = v[2];
    let a = v[3];
    let b = v[4];

    let mut l = 1.0;
    let mut r = t;
    while r - l > 1e-3 {
        let d = (r - l) / 3.0;
        let xl = l + d;
        let xr = r - d;

        let fl = b * n / xl + a * xl * (xl - 1.0) / 4.0;
        let fr = b * n / xr + a * xr * (xr - 1.0) / 4.0;

        // println!("{l} {r} :: {xl}:{fl}, {xr}:{fr}");

        if fl < fr {
            r = xr;
        } else {
            l = xl;
        }
    }
    // println!("{l} {r}");
    // println!("df/dx {l} {}", -b * n / (l * l) + a / 4.0 * (2.0 * l - 1.0));
    // println!("df/dx {r} {}", -b * n / (r * r) + a / 4.0 * (2.0 * r - 1.0));

    let mut ans = f64::MAX;
    if s <= t {
        ans = (t - s) * a;
    }

    let l = l as i64;
    for x in (l - 10000000)..(l + 10000000) {
        let x = x as f64;
        if x < 1.0 || t < x {
            continue;
        }
        let f = b * n / x + a * x * (x - 1.0) / 4.0;

        // println!("{x} {f}");

        if f < ans {
            ans = f;
        }
    }

    println!("{ans}");

    // 1 <= x <= T
    // p = x / N
    // s      = 1p + 2p(1-p) + 3p(1-p)^2 + ..
    // s(1-p) =      1p(1-p) + 2p(1-p)^2 + ..
    // sp     =  p +  p(1-p) + 2p(1-p)^2 + ..
    // s      =  1 + (1-p) + (1-p)^2 + ..
    // s      =  p^-1
    //        = N / x

    // t = (0 + 1 + 2 + .. (x-1))/2 = x(x-1)/4

    // f     = As + Bt
    //       = AN / x + Bx(x-1)/4
    // df/dx = -ANx^-2 + Bx/2 - B/4
}
