fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let n = read_line().parse().unwrap();

    if n % 3 == 2 || n <= 4 {
        println!("No");
        return;
    }

    let mut ans = vec![vec![0; n]; n];

    let m = n * (n - 1) / 6;
    let mut nr = m;

    let mut i = n - 1;
    loop {
        if i > nr {
            break;
        }

        for j in 0..i {
            ans[i][j] = 1;
            ans[j][i] = 1;
        }

        nr -= i;
        i -= 1;
    }
    let p = i;

    let mut i = 0;
    loop {
        for j in 0..i {
            ans[i][j] = 1;
            ans[j][i] = 1;
            nr -= 1;

            if nr == 0 {
                break;
            }
        }

        if nr == 0 {
            break;
        }

        i += 1;
    }
    let q = i;

    let mut nb = m;
    for i in 0..=p {
        let c = 2 + i % 2;
        for j in 0..=q {
            if i <= j || ans[i][j] != 0 {
                continue;
            }

            ans[i][j] = c;
            ans[j][i] = c;

            if c == 2 {
                nb -= 1;
            }
        }
    }

    for i in 0..n {
        for j in 0..i {
            if ans[i][j] != 0 {
                continue;
            }
            let c = if nb > 0 { 2 } else { 3 };
            if c == 2 {
                nb -= 1;
            }
            ans[i][j] = c;
            ans[j][i] = c;
        }
    }

    println!("Yes");
    for h in 0..n - 1 {
        let aa = &ans[h][h + 1..].into_iter().map(|&c| {
            if c == 1 {
                "R"
            } else if c == 2 {
                "B"
            } else {
                "W"
            }
        });
        let aa: Vec<_> = aa.clone().collect();
        let aa = aa.join("");
        println!("{aa}");
        // println!("{h} {:?}", aa);
    }
    // println!("q: {q}, p: {p}, nb: {nb}");
}
