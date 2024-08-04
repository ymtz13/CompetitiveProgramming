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

fn split(aa: &Vec<usize>) -> (Vec<usize>, usize, usize) {
    let hh0: Vec<_> = aa.iter().map(|a| (a + WIDTH - 1) / WIDTH).collect();
    let sh0 = hh0.iter().fold(0, |acc, c| acc + c);

    let mut rh: Vec<_> = aa
        .iter()
        .enumerate()
        .filter(|(_, &a)| a > WIDTH)
        .map(|(i, &a)| (i, (a - 1) % WIDTH))
        .collect();
    rh.sort_by_key(|&(_, a)| a);

    let mut overflow = if sh0 > WIDTH { sh0 - WIDTH } else { 0 };
    let mut hh: Vec<_> = hh0.iter().cloned().collect();
    let mut penalty = 0;

    for &(i, r) in rh.iter() {
        if overflow <= 0 {
            break;
        };

        hh[i] -= 1;
        overflow -= 1;
        penalty += r;
    }

    for h in hh.iter_mut() {
        if overflow <= 0 {
            break;
        };

        let v = std::cmp::min(*h - 1, overflow);
        *h -= v;
        overflow -= v;
        penalty += v * WIDTH;
    }
    let sh = hh.iter().fold(0, |acc, h| acc + h);

    // println!("{} {:?}", sh0, hh0);
    // println!("{} {} {:?}", sh, penalty, hh);

    (hh, sh, penalty)
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
