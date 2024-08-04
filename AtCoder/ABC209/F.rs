static MOD: usize = 1_000_000_007;

fn read_line() -> String {
    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();
    String::from(inp.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let _n: usize = read_line().parse().unwrap();
    let hh = read_vec();
    let mut aa = vec![1];

    let mut ph = hh[0];
    for &h in &hh[1..] {
        let sum = aa.iter().fold(0, |p, q| (p + q) % MOD);
        let acc = aa.iter().fold(vec![0], |mut acc, &v| {
            acc.push((acc[acc.len() - 1] + v) % MOD);
            acc
        });

        if h == ph {
            aa = vec![sum; aa.len() + 1];
        }
        if h < ph {
            aa = acc.iter().map(|c| (MOD + sum - c) % MOD).collect();
        }
        if h > ph {
            aa = acc;
        }
        ph = h;
    }

    let sum = aa.iter().fold(0, |p, q| (p + q) % MOD);
    println!("{}", sum);
}
