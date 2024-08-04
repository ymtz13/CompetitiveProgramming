const MOD: usize = 998244353;

fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let nk = read_vec();
    let n = nk[0];
    let k = nk[1];

    let m = 1_000_010;
    let mut dd: Vec<_> = (0..m).collect();
    let mut primes = vec![];
    for p in 2..m {
        if dd[p] != p {
            continue;
        }
        primes.push(p);
        let mut i = p;
        while i < m {
            dd[i] = p;
            i += p;
        }
    }

    let n0 = n - k + 1;

    let mut cc = vec![0; primes.len()];
    let mut xx: Vec<_> = (n0..=n).into_iter().collect();

    for (ip, &p) in primes.iter().enumerate() {
        let i0 = if n0 % p == 0 { 0 } else { p - (n0 % p) };
        let mut i = i0;
        while i < k {
            while xx[i] % p == 0 {
                cc[ip] += 1;
                xx[i] /= p;
            }
            i += p;
        }
    }

    for (ip, &p) in primes.iter().enumerate() {
        let mut i = p;
        while i <= k {
            let mut x = i;
            while x % p == 0 {
                cc[ip] -= 1;
                x /= p;
            }
            i += p;
        }
    }

    let mut ans = 1;
    for &c in &cc {
        ans *= c + 1;
        ans %= MOD;
    }

    for &x in &xx {
        if x > 1 {
            ans *= 2;
            ans %= MOD;
        }
    }

    println!("{ans}");
}
