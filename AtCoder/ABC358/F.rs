fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uuu() -> (usize, usize, usize) {
    let v = read_vec();
    (v[0], v[1], v[2])
}

fn no() {
    println!("No");
}

fn yes(ans: Vec<Vec<&str>>) {
    println!("Yes");
    for row in &ans {
        println!("{}", row.join(""));
    }
}

fn main() {
    let (n, m, k) = read_uuu();
    if k < n {
        no();
        return;
    }
    let n2 = n * 2;
    let m2 = m * 2;

    let mut ans = vec![vec!["+"; m2 + 1]; n2 + 1];
    ans[0][m2 - 1] = "S";
    ans[n2][m2 - 1] = "G";

    for i in 0..n {
        for j in 0..m {
            ans[i * 2 + 1][j * 2 + 1] = "o";
            if i > 0 {
                ans[i * 2][j * 2 + 1] = "-";
            }
            if j > 0 {
                ans[i * 2 + 1][j * 2] = "|";
            }
        }
    }

    for i in 1..n {
        ans[i * 2][m2 - 1] = ".";
    }

    if n % 2 == 0 {
        if k % 2 == 1 {
            no();
            return;
        }

        let mut x = (k - n) / 2;

        for i in 0..n {
            if i % 2 == 1 {
                continue;
            }
            for j in (0..m - 1).rev() {
                if x == 0 {
                    break;
                }
                x -= 1;
                let r0 = i * 2 + 1;
                let r1 = r0 + 2;
                let c0 = j * 2 + 1;
                ans[r0][c0 + 1] = ".";
                ans[r1][c0 + 1] = ".";
                ans[r0 + 1][c0] = ".";
                ans[r0 + 1][c0 + 2] = "-";
            }
        }
    } else {
        if k % 2 == 0 {
            no();
            return;
        }

        if m % 2 == 1 {
            let mut x = (k - n) / 2;

            for j in (0..m - 1).rev() {
                if x == 0 {
                    break;
                }
                x -= 1;
                let r0 = (n - 2) * 2 + 1;
                let r1 = r0 + 2;
                let c0 = j * 2 + 1;
                ans[r0][c0 + 1] = ".";
                ans[r1][c0 + 1] = ".";
                ans[r0 + 1][c0] = ".";
                ans[r0 + 1][c0 + 2] = "-";
            }

            for j in 0..m - 1 {
                if j % 2 == 1 {
                    continue;
                }
                for i in (0..n - 2).rev() {
                    if x == 0 {
                        break;
                    }
                    x -= 1;
                    let c0 = j * 2 + 1;
                    let c1 = c0 + 2;
                    let r0 = i * 2 + 1;
                    ans[r0 + 1][c0] = ".";
                    ans[r0 + 1][c1] = ".";
                    ans[r0][c0 + 1] = ".";
                    ans[r0 + 2][c0 + 1] = "|";
                }
            }
        } else {
            let mut x = (k - n) / 2;

            for i in 0..n - 1 {
                if i % 2 == 1 {
                    continue;
                }
                for j in (0..m - 1).rev() {
                    if x == 0 {
                        break;
                    }
                    x -= 1;
                    let r0 = i * 2 + 1;
                    let r1 = r0 + 2;
                    let c0 = j * 2 + 1;
                    ans[r0][c0 + 1] = ".";
                    ans[r1][c0 + 1] = ".";
                    ans[r0 + 1][c0] = ".";
                    ans[r0 + 1][c0 + 2] = "-";
                }
            }

            for j in 0..m - 1 {
                if j % 2 == 1 {
                    continue;
                }
                if x == 0 {
                    break;
                }
                x -= 1;
                let c0 = j * 2 + 1;
                let c1 = c0 + 2;
                let r0 = (n - 1) * 2 + 1;
                ans[r0 - 1][c0] = ".";
                ans[r0 - 1][c1] = ".";
                ans[r0][c0 + 1] = ".";
                ans[r0 - 2][c0 + 1] = "|";
            }
        }
    }

    yes(ans);
}
