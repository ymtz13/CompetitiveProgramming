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

    let mut aaa: Vec<Vec<(usize, usize)>> = vec![];

    for _ in 0..days {
        let mut aa: Vec<_> = read_vec().into_iter().enumerate().collect();
        aa.sort_by_key(|&(_, a)| a);
        aa.reverse();
        aaa.push(aa);
    }
    // println!("{:?}", aaa);

    let mut aamax = vec![0; num];
    for aa in aaa.iter() {
        for (i, &(_, a)) in aa.iter().enumerate() {
            aamax[i] = std::cmp::max(aamax[i], a);
        }
    }
    // println!("{:?}", aamax);

    let mut s = 0;
    let mut hh = vec![];
    for (_, amax) in aamax.iter().enumerate() {
        let dh = (amax + width - 1) / width;
        hh.push((s, s + dh));
        s = s + dh;
    }
    // println!("{:?}", hh);

    for aa in aaa.iter() {
        for (i, _) in aa.iter() {
            let (h0, h1) = hh[*i];
            if h1 >= width {
                if h0 <= width - 2 {
                    println!("{} {} {} {}", h0, 0, width - 1, width);
                } else {
                    let ww = width / num;
                    println!("{} {} {} {}", width - 1, i * ww, width, (i + 1) * ww);
                }
            } else {
                println!("{} {} {} {}", h0, 0, h1, width);
            }
        }
    }
}
