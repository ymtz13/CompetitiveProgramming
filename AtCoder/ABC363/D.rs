fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn main() {
    let mut n = read_vec()[0];

    if n == 1 {
        println!("0");
        return;
    }
    n -= 1;

    let mut z = 1;
    for d in 1..100 {
        let e = (d + 1) / 2;
        let t = 9 * z;
        if d % 2 == 1 {
            if n <= t {
                let x = z + n - 1;
                let x = x.to_string();
                let mut ans = x.clone();

                for i in (0..d / 2).rev() {
                    ans.push_str(x.get(i..=i).unwrap());
                }

                println!("{ans}");
                break;
            } else {
                n -= t;
            }
        } else {
            if n <= t {
                let x = z + n - 1;
                let x = x.to_string();
                let mut ans = x.clone();

                for i in (0..d / 2).rev() {
                    ans.push_str(x.get(i..=i).unwrap());
                }

                println!("{ans}");
                break;
            } else {
                n -= t;
            }

            z *= 10;
        }
    }
}
