fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

#[derive(Debug)]
struct Point(f64, f64);

impl Point {
    fn radius(&self) -> f64 {
        let Point(x, y) = self;
        (x * x + y * y).sqrt()
    }

    fn arg(&self) -> f64 {
        let Point(x, y) = self;
        let sign = if *y >= 0.0 { 1.0 } else { -1.0 };
        (x / self.radius()).acos() * sign
    }
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let mut pp = vec![];

    for _ in 0..n {
        let s: Vec<_> = read_line().split_whitespace().map(|v| v.parse().unwrap()).collect();
        pp.push(Point(s[0], s[1]));
    }

    let mut cnt0 = 0;
    let mut cnt1 = 0;
    for i0 in 0..n {
        let mut qq = vec![];
        let Point(x0, y0) = pp[i0];
        for i in 0..n {
            if i != i0 {
                let Point(x, y) = pp[i];
                qq.push(Point(x - x0, y - y0).arg());
            }
        }
        qq.sort_by(|a, b| a.partial_cmp(b).unwrap());

        use std::f64::consts::TAU;
        let qq2: Vec<_> = qq.iter().map(|c| c + TAU).collect();
        qq.extend(qq2);

        // println!("{i0}, {qq:?}");

        let eps = 1e-10;

        let mut r = 0;
        for l in 0..n - 1 {
            while r + 1 < qq.len() && qq[r + 1] - qq[l] < TAU / 4.0 + eps {
                r += 1;
            }

            if qq[r] - qq[l] > TAU / 4.0 - eps {
                cnt1 += 1;
                cnt0 += r - l - 1;
                // println!("= 90deg {l} {r}");
            } else {
                cnt0 += r - l;
                // println!("< 90deg {l} {r}");
            }
        }
    }

    let all = n * (n - 1) * (n - 2);
    let cnt2 = all / 2 - cnt0 - cnt1;
    println!("{} {} {}", all / 6 - (cnt1 + cnt2), cnt1, cnt2);
}
