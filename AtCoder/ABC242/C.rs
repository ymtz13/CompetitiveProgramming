const MOD: usize = 998244353;

fn main() {
    let (n,): (usize,) = Read::read();
    let mut dp = vec![1; 11];
    dp[0] = 0;
    dp[10] = 0;

    for _ in 1..n {
        let mut dp_next = vec![0; 11];
        for i in 1..=9 {
            dp_next[i] = (dp[i - 1] + dp[i] + dp[i + 1]) % MOD;
        }
        dp = dp_next;
        println!("{:?}", dp);
    }

    let ans = dp.iter().sum::<usize>() % MOD;

    println!("{}", ans);
}

//=============================================================================

fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

trait Read {
    fn read() -> Self;
}

impl<T1> Read for (T1,)
where
    T1: std::str::FromStr,
{
    fn read() -> (T1,) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();

        if let Ok(v1) = v1 {
            return (v1,);
        }

        panic!();
    }
}

impl<T1, T2> Read for (T1, T2)
where
    T1: std::str::FromStr,
    T2: std::str::FromStr,
{
    fn read() -> (T1, T2) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();
        let v2 = s.next().unwrap().parse();

        if let (Ok(v1), Ok(v2)) = (v1, v2) {
            return (v1, v2);
        }

        panic!();
    }
}

impl<T1, T2, T3> Read for (T1, T2, T3)
where
    T1: std::str::FromStr,
    T2: std::str::FromStr,
    T3: std::str::FromStr,
{
    fn read() -> (T1, T2, T3) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();
        let v2 = s.next().unwrap().parse();
        let v3 = s.next().unwrap().parse();

        if let (Ok(v1), Ok(v2), Ok(v3)) = (v1, v2, v3) {
            return (v1, v2, v3);
        }

        panic!();
    }
}

impl<T1, T2, T3, T4> Read for (T1, T2, T3, T4)
where
    T1: std::str::FromStr,
    T2: std::str::FromStr,
    T3: std::str::FromStr,
    T4: std::str::FromStr,
{
    fn read() -> (T1, T2, T3, T4) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();
        let v2 = s.next().unwrap().parse();
        let v3 = s.next().unwrap().parse();
        let v4 = s.next().unwrap().parse();

        if let (Ok(v1), Ok(v2), Ok(v3), Ok(v4)) = (v1, v2, v3, v4) {
            return (v1, v2, v3, v4);
        }

        panic!();
    }
}

impl<T1, T2, T3, T4, T5> Read for (T1, T2, T3, T4, T5)
where
    T1: std::str::FromStr,
    T2: std::str::FromStr,
    T3: std::str::FromStr,
    T4: std::str::FromStr,
    T5: std::str::FromStr,
{
    fn read() -> (T1, T2, T3, T4, T5) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();
        let v2 = s.next().unwrap().parse();
        let v3 = s.next().unwrap().parse();
        let v4 = s.next().unwrap().parse();
        let v5 = s.next().unwrap().parse();

        if let (Ok(v1), Ok(v2), Ok(v3), Ok(v4), Ok(v5)) = (v1, v2, v3, v4, v5) {
            return (v1, v2, v3, v4, v5);
        }

        panic!();
    }
}

impl<T1, T2, T3, T4, T5, T6> Read for (T1, T2, T3, T4, T5, T6)
where
    T1: std::str::FromStr,
    T2: std::str::FromStr,
    T3: std::str::FromStr,
    T4: std::str::FromStr,
    T5: std::str::FromStr,
    T6: std::str::FromStr,
{
    fn read() -> (T1, T2, T3, T4, T5, T6) {
        let s = input();
        let mut s = s.split_whitespace();
        let v1 = s.next().unwrap().parse();
        let v2 = s.next().unwrap().parse();
        let v3 = s.next().unwrap().parse();
        let v4 = s.next().unwrap().parse();
        let v5 = s.next().unwrap().parse();
        let v6 = s.next().unwrap().parse();

        if let (Ok(v1), Ok(v2), Ok(v3), Ok(v4), Ok(v5), Ok(v6)) = (v1, v2, v3, v4, v5, v6) {
            return (v1, v2, v3, v4, v5, v6);
        }

        panic!();
    }
}
