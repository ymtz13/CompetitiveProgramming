fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn xor(x: &Vec<u8>, y: &Vec<u8>) -> Vec<u8> {
    x.iter().zip(y.iter()).map(|(x, y)| x ^ y).collect()
}

fn main() {
    let n: usize = read_line().parse().unwrap();

    let mut sss = vec![];
    for _ in 0..n {
        let ss = read_line();
        sss.push(ss.bytes().map(|c| c - b'0').collect::<Vec<_>>());
    }

    let mut dd = vec![false; n];

    for p in 0..n {
        let mut ok = false;
        for i in 0..n {
            if dd[i] {
                continue;
            }

            if sss[i][p] == 1 {
                ok = true;
                dd[i] = true;
                for j in 0..n {
                    if i == j {
                        continue;
                    }
                    if sss[j][p] == 1 {
                        sss[j] = xor(&sss[i], &sss[j]);
                    }
                }
                break;
            }
        }

        if !ok {
            println!("Even");
            return;
        }
    }

    println!("Odd");
}
