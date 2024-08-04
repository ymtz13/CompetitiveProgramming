fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let n: usize = read_line().parse().unwrap();
    let mut aa = read_vec();
    aa.sort();

    let m = 100_000_000;
    let mut ans = aa.iter().sum::<usize>() * (n - 1);

    aa.push(m);

    let mut cnt = 0;
    let mut j = n;
    for i in 0..n {
        while j - 1 > i && aa[i] + aa[j - 1] >= m {
            j -= 1;
        }
        if j <= i {
            j = i + 1
        }

        cnt += n - j;
    }

    ans -= cnt * m;

    println!("{ans}");
}
