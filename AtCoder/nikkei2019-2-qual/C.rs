fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let n = read_vec()[0];
    let aa = read_vec();
    let bb = read_vec();

    let mut ai: Vec<_> = aa.iter().enumerate().map(|(i, a)| (a, i)).collect();
    ai.sort();

    let mut bi: Vec<_> = bb.iter().enumerate().map(|(i, b)| (b, i)).collect();
    bi.sort();

    // println!("{bi:?}");

    let mut tt = vec![0; n];

    for j in 0..n {
        let (a, ia) = ai[j];
        let (b, ib) = bi[j];

        if a > b {
            println!("No");
            return;
        }

        tt[ia] = ib;
    }

    let mut s = 0;
    let mut cnt = 0;
    loop {
        cnt += 1;
        s = tt[s];
        if s == 0 {
            break;
        }
    }

    // println!("{tt:?}");
    // println!("{cnt}");

    if cnt < n {
        println!("Yes");
        return;
    }

    for j in 1..n {
        let (a, _) = ai[j];
        let (b, _) = bi[j - 1];

        if a <= b {
            println!("Yes");
            return;
        }
    }

    println!("No");
}
