fn input() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input
}

fn read_int_vec() -> Vec<i32> {
    input()
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect()
}

fn main() {
    let hw = read_int_vec();
    let h = hw[0];
    let w = hw[1];

    let mut atable = Vec::new();
    for _ in 0..h {
        atable.push(read_int_vec());
    }

    let mut ans = std::i32::MAX;

    for th in 0..h {
        for tw in 0..w {
            let mut sum = 0;
            for ih in 0..h {
                for iw in 0..w {
                    let d = std::cmp::min(i32::abs(th - ih), i32::abs(tw - iw));
                    sum += d * atable[ih as usize][iw as usize];
                    // println!("  {} {} {}", ih, iw, d);
                }
            }
            // println!("{} {} {}\n", th, tw, sum);
            ans = std::cmp::min(ans, sum);
        }
    }

    // println!("{:?}", atable);
    println!("{}", ans);
}
