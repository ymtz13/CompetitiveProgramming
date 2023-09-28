fn main() {
    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();

    let p: usize = inp.trim().parse().unwrap();

    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();
    let n: usize = inp.trim().parse().unwrap();

    let mut a = vec![0; p];
    for x in 0..p {
        a[power(x, n, p)] += 1;
    }

    let mut ans = 0;
    for (x, nx) in a.iter().enumerate() {
        for (y, ny) in a.iter().enumerate() {
            let z = (x + y) % p;
            let nz = a[z];
            ans += nx * ny * nz;
        }
    }

    println!("{}", ans);
}

fn power(mut x: usize, mut n: usize, p: usize) -> usize {
    if x == 0 {
        return 0;
    }

    let mut r = 1;

    while n > 0 {
        if n & 1 > 0 {
            r *= x;
            r %= p;
        }
        x *= x;
        x %= p;
        n >>= 1;
    }

    r
}
