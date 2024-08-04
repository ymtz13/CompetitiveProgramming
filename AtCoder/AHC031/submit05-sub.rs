static WIDTH: usize = 1000;

fn read_vec() -> Vec<usize> {
    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();
    inp.split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn take_max(aaa: &[Vec<usize>]) -> Vec<usize> {
    let mut aamax = vec![0; aaa[0].len()];

    for aa in aaa.iter() {
        for (i, a) in aa.iter().enumerate() {
            aamax[i] = std::cmp::max(aamax[i], *a);
        }
    }

    aamax
}

fn pack(aa: &Vec<(usize, usize)>) -> (usize, Vec<(usize, usize)>, i64) {
    let row_max = aa.iter().map(|&(_, a)| (a + WIDTH - 1) / WIDTH).fold(0, |acc, row| acc + row);

    for row in row_max - aa.len()..=row_max {
        let cols: Vec<_> = aa.iter().map(|&(i, a)| (i, (a + row - 1) / row)).collect();
        let scols = cols.iter().fold(0, |acc, &(_, col)| acc + col);

        if scols < WIDTH {
            return (row, cols, row_max - row);
        }
    }

    panic!();
}

fn split(aa: &Vec<usize>) -> Vec<(usize, Vec<(usize, usize)>)> {
    let hh0: Vec<_> = aa.iter().map(|a| (a + WIDTH - 1) / WIDTH).collect();
    let sh0 = hh0.iter().fold(0, |acc, c| acc + c);
    let mut excess = sh0 as i64 - WIDTH as i64;

    if excess <= 0 {
        return hh0.iter().enumerate().map(|&(i, h)| (h, vec![(i, WIDTH)])).collect();
    }

    let mut aa: Vec<_> = aa.iter().enumerate().collect();
    aa.sort_by_key(|&(_, a)| a % WIDTH);
}

fn main() {
    let wdn = read_vec();
    let days = wdn[1];
    let _num = wdn[2];

    let aaa: Vec<_> = (0..days).map(|_| read_vec()).collect();

    let mut day_l = 0;
    while day_l < days {
        let mut day_r_max = day_l + 1;

        for day_r in day_l + 2..days {
            let aa = take_max(&aaa[day_l..day_r]);
            let (_hh, _sh, penalty) = split(&aa);

            if penalty > 0 {
                break;
            }

            day_r_max = day_r;
        }

        let aa = take_max(&aaa[day_l..day_r_max]);
        let (hh, _sh, penalty) = split(&aa);
        // println!("{} -> {}, penalty={}", day_l, day_r_max, penalty);

        for _ in day_l..day_r_max {
            let mut h0 = 0;
            for h in hh.iter() {
                println!("{} {} {} {}", h0, 0, h0 + h, WIDTH);
                h0 += h;
            }
        }

        day_l = day_r_max;
    }

    // take_max(&aaa[2..7]);

    // for aa in aaa.iter() {
    //     let (hh, _sh, _penalty) = split(aa);

    //     let mut h0 = 0;
    //     for h in hh.iter() {
    //         println!("{} {} {} {}", h0, 0, h0 + h, WIDTH);
    //         h0 += h;
    //     }
    // }
}
