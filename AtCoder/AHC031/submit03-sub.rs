fn read_vec() -> Vec<usize> {
    let mut inp = String::new();
    std::io::stdin().read_line(&mut inp).unwrap();
    inp.split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let wdn = read_vec();
    let width = wdn[0];
    let days = wdn[1];
    let num = wdn[2];
    // println!("{:?}", (width, days, num));

    let mut aaa: Vec<Vec<usize>> = vec![];

    for _ in 0..days {
        aaa.push(read_vec());
    }
    // println!("{:?}", aaa);

    for aa in aaa.iter() {
        let hh0: Vec<_> = aa.iter().map(|a| (a + width - 1) / width).collect();
        let sh0 = hh0.iter().fold(0, |acc, c| acc + c);

        let mut rh: Vec<_> = aa
            .iter()
            .enumerate()
            .filter(|(_, &a)| a > width)
            .map(|(i, &a)| (i, (a - 1) % width))
            .collect();
        rh.sort_by_key(|&(_, a)| a);

        let mut overflow = if sh0 > width { sh0 - width } else { 0 };
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
            penalty += v * width;
        }
        let sh = hh.iter().fold(0, |acc, h| acc + h);

        // println!("{} {:?}", sh0, hh0);
        // println!("{} {} {:?}", sh, penalty, hh);

        let mut h0 = 0;
        for h in hh.iter() {
            println!("{} {} {} {}", h0, 0, h0 + h, width);
            h0 += h;
        }
    }
}
