fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (usize, usize) {
    let v = read_vec();
    (v[0], v[1])
}

fn main() {
    let mut n: usize = read_line().parse().unwrap();
    let m = 3usize.pow(n as u32);

    let mut ans = vec![vec![0; m]; m];
    ans[0][0] = 1;

    let aa = vec![(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)];

    for k in 0..n {
        let l = 3usize.pow(k as u32);
        let l3 = l * 3;
        for &(ax, ay) in &aa {
            for dx in 0..l {
                for dy in 0..l {
                    ans[dx + ax * l][dy + ay * l] = ans[dx][dy];
                }
            }
        }
    }

    for row in &ans {
        let row: Vec<_> = row.iter().map(|c| if *c == 0 { "." } else { "#" }).collect();
        println!("{}", row.join(""));
    }
}
