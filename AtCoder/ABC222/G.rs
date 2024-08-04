fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn euclidean(mut a: i64, mut b: i64) -> (i64, (i64, i64)) {
    let mut u00 = 1;
    let mut u01 = 0;
    let mut u10 = 0;
    let mut u11 = 1;

    while b > 0 {
        let q = a / b;
        let r = a % b;

        (u00, u01, u10, u11) = (u10, u11, u00 - q * u10, u01 - q * u11);

        a = b;
        b = r;
    }

    (a, (u00, u01))
}

fn inv10(k: usize) -> usize {
    let kk = k as i64;
    let (_, (_, r)) = euclidean(kk, 10);
    ((r % kk) + kk) as usize % k
}

fn main() {
    let t: usize = read_line().parse().unwrap();
    for _ in 0..t {
        let k: usize = read_line().parse().unwrap();

        if k % 4 == 0 || k % 5 == 0 {
            println!("-1");
            continue;
        }
        let k = if k % 2 == 0 { k / 2 } else { k };

        if k == 1 {
            println!("1");
            continue;
        }

        let mut m = 1;
        let mut a = 10;
        let mut b = 1;
        while m * m <= k {
            m *= 2;
            (a, b) = (a * a % k, (a + 1) * b % k);
        }

        let r = inv10(k);
        let mut v = 0;
        let mut map = std::collections::HashMap::new();
        map.insert(0, 0);
        for i in 1..=m {
            v = (v + k - 1) * r % k;
            if !map.contains_key(&v) {
                map.insert(v, i);
            }
        }

        let mut v = 1;
        let mut ans = -1;
        for i in 0..=m {
            if let Some(j) = map.get(&v) {
                ans = 1 + (i * m + j) as i64;
                break;
            }
            v = (a * v + b) % k;
        }

        println!("{ans}");
    }
}
