// gcd(a, b) と ax + by = gcd(a, b) を満たす x, y を返す
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

fn main() {
    for &(a, b) in &vec![(66, 54), (10, 2347)] {
        let (gcd, (x, y)) = euclidean(a, b);
        println!("{gcd} = {a} * {x} + {b} * {y} = {} + {} = {}", a * x, b * y, a * x + b * y);
    }
}
