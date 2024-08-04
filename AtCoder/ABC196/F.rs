fn read_line() -> String {
    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();
    String::from(inp.trim())
}

fn read_string() -> Vec<u8> {
    read_line().bytes().collect()
}

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

fn fft(n: usize, aa: Vec<Complex>, inverse: bool) -> Vec<Complex> {
    if n == 1 {
        return Vec::from(aa);
    }

    let aa0: Vec<_> = aa.iter().enumerate().filter(|(i, _)| i % 2 == 0).map(|(_, a)| a.clone()).collect();
    let aa1: Vec<_> = aa.iter().enumerate().filter(|(i, _)| i % 2 == 1).map(|(_, a)| a.clone()).collect();

    let nn = n >> 1;
    let bb0 = fft(nn, aa0, inverse);
    let bb1 = fft(nn, aa1, inverse);

    let sign = if inverse { 1.0 } else { -1.0 };
    let k = sign * std::f64::consts::TAU / (n as f64);
    let ww = (0..nn).map(|i| Complex::expi(k * (i as f64)));

    let zip: Vec<_> = ww.zip(bb0.iter().zip(bb1.iter())).map(|(w, (b0, b1))| (w, *b0, *b1)).collect();

    let r0: Vec<_> = zip.iter().map(|&(w, b0, b1)| b0 + w * b1).collect();
    let r1: Vec<_> = zip.iter().map(|&(w, b0, b1)| b0 - w * b1).collect();

    vec![r0, r1].concat()
}

fn main() {
    let mut s: Vec<i64> = read_string().iter().map(|c| 1 - 2 * (c - b'0') as i64).collect();
    let mut t: Vec<i64> = read_string().iter().map(|c| 1 - 2 * (c - b'0') as i64).collect();
    t.reverse();

    let len_s = s.len();
    let len_t = t.len();

    let mut n = 1;
    while n < len_s * 2 + 1 {
        n <<= 1;
    }

    s.extend(vec![0; n - len_s]);
    t.extend(vec![0; n - len_t]);

    let s: Vec<_> = s.iter().map(|&v| Complex { re: (v as f64), im: 0.0 }).collect();
    let t: Vec<_> = t.iter().map(|&v| Complex { re: (v as f64), im: 0.0 }).collect();
    // println!("s: {:?}", s);
    // println!("t: {:?}", t);

    let fs = fft(n, s, false);
    let ft = fft(n, t, false);
    // println!("fs: {:?}", fs);
    // println!("ft: {:?}", ft);

    let fst: Vec<_> = fs.iter().zip(ft.iter()).map(|(&s, &t)| s * t).collect();
    let st = fft(n, fst.clone(), true);
    // println!("fst: {:?}", fst);
    // println!(" st: {:?}", st);

    let st = &st[len_t - 1..len_s];
    // println!("{:?}", st);

    let v = st.iter().map(|c| c.re.round() as i64).map(|c| c / (n as i64)).reduce(std::cmp::max).unwrap();
    println!("{:?}", ((len_t as i64) - v) / 2);

    // println!("{:?}", s);
    // println!("{:?}", t);
}
