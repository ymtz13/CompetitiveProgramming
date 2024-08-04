#[derive(Copy, Clone, Debug)]
struct Complex {
    re: f64,
    im: f64,
}

impl Complex {
    fn expi(theta: f64) -> Complex {
        Complex {
            re: theta.cos(),
            im: theta.sin(),
        }
    }
}

impl std::ops::Mul for Complex {
    type Output = Self;

    fn mul(self, rhs: Self) -> Self {
        Self {
            re: self.re * rhs.re - self.im * rhs.im,
            im: self.re * rhs.im + self.im * rhs.re,
        }
    }
}

impl std::ops::Add for Complex {
    type Output = Self;

    fn add(self, rhs: Self) -> Self {
        Self {
            re: self.re + rhs.re,
            im: self.im + rhs.im,
        }
    }
}

impl std::ops::Neg for Complex {
    type Output = Self;

    fn neg(self) -> Self {
        Self { re: -self.re, im: -self.im }
    }
}

impl std::ops::Sub for Complex {
    type Output = Self;

    fn sub(self, rhs: Self) -> Self {
        self + (-rhs)
    }
}

fn fft(n: usize, aa: &Vec<Complex>, inverse: bool) -> Vec<Complex> {
    if n == 1 {
        return aa.clone();
    }

    let aa0: Vec<_> = aa.iter().enumerate().filter(|(i, _)| i % 2 == 0).map(|(_, a)| a.clone()).collect();
    let aa1: Vec<_> = aa.iter().enumerate().filter(|(i, _)| i % 2 == 1).map(|(_, a)| a.clone()).collect();

    let nn = n >> 1;
    let bb0 = fft(nn, &aa0, inverse);
    let bb1 = fft(nn, &aa1, inverse);

    let sign = if inverse { 1.0 } else { -1.0 };
    let k = sign * std::f64::consts::TAU / (n as f64);
    let ww = (0..nn).map(|i| Complex::expi(k * (i as f64)));

    let zip: Vec<_> = ww.zip(bb0.iter().zip(bb1.iter())).map(|(w, (b0, b1))| (w, *b0, *b1)).collect();

    let r0: Vec<_> = zip.iter().map(|&(w, b0, b1)| b0 + w * b1).collect();
    let r1: Vec<_> = zip.iter().map(|&(w, b0, b1)| b0 - w * b1).collect();

    vec![r0, r1].concat()
}

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<i64> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let aa = read_vec();
    let bb = read_vec();

    let mut m = 1;
    while m < n * 2 + 1 {
        m *= 2;
    }

    let mut vv = vec![0; n];

    for i in 0..5 {
        let mut xaa: Vec<_> = aa.iter().map(|v| 1 - (v >> i) & 1).collect();
        let mut xbb: Vec<_> = bb.iter().map(|v| 1 - (v >> i) & 1).collect();
        xbb.reverse();

        xaa.extend(vec![0; m - n]);
        xbb.extend(vec![0; m - n]);

        // println!("{:?}", (i, xaa.clone()));
        // println!("{:?}", (i, xbb.clone()));

        let xaa: Vec<_> = xaa.iter().map(|&v| Complex { re: v as f64, im: 0.0 }).collect();
        let xbb: Vec<_> = xbb.iter().map(|&v| Complex { re: v as f64, im: 0.0 }).collect();
        // xbb.reverse();

        let faa = fft(m, &xaa, false);
        let fbb = fft(m, &xbb, false);

        let fab: Vec<_> = faa.iter().zip(fbb.iter()).map(|(&va, &vb)| va * vb).collect();
        let xab = fft(m, &fab, true);

        let xaa: Vec<_> = xaa.iter().map(|c| c.re.round()).collect();
        let xbb: Vec<_> = xbb.iter().map(|c| c.re.round()).collect();
        let xab: Vec<_> = xab.iter().map(|c| (c.re.round() / (m as f64)) as i64).collect();

        // println!("{:?}", (i, xaa, xbb, xab));
        // println!("{:?}", (i, xab.clone()));

        let mut ww = vec![n as i64; n];
        for (i, x) in xab[0..2 * n - 1].iter().enumerate() {
            ww[i % n] -= x;
        }
        // println!("{:?}", (i, ww.clone()));

        for (j, x) in ww.iter().enumerate() {
            vv[j] += x << i;
        }
        // println!("{:?}", (i, vv.clone()));
    }

    println!("{}", vv.iter().max().unwrap());
}
