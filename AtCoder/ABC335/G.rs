fn pow(mut x: u128, mut y: u128, m: u128) -> u128 {
    let mut r = 1;

    while y > 0 {
        if y & 1 == 1 {
            r *= x;
            r %= m;
        }
        x *= x;
        x %= m;
        y >>= 1;
    }

    r
}

fn main() {
    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();

    let np: Vec<u128> = inp
        .trim()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect();

    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();

    let aa: Vec<u128> = inp
        .trim()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect();

    let p = np[1];
    let q = p - 1;
    let mut divisors = std::collections::HashSet::new();

    for i in 1..=q {
        if i * i > q {
            break;
        }

        if q % i == 0 {
            divisors.insert(i);
            divisors.insert(q / i);
        }
    }

    let mut divisors = divisors.into_iter().collect::<Vec<_>>();
    divisors.sort();

    let mut counts = std::collections::HashMap::new();

    for a in aa {
        for divisor in &divisors {
            if pow(a, *divisor, p) == 1 {
                let x = q / divisor;
                *counts.entry(x).or_insert(0) += 1;
                break;
            }
        }
    }

    println!("{:#?}", counts);

    let mut ans = 0;
    for (x, cx) in counts.iter() {
        for (y, cy) in counts.iter() {
            if y % x == 0 {
                ans += cx * cy;
            }
            println!("{:?} {:?}", (x, cx), (y, cy))
        }
    }

    println!("{}", ans);
}
