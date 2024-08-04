fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<String> {
    read_line().split_whitespace().map(|c| String::from(c)).collect()
}

use std::collections::VecDeque;

fn main() {
    let ql = read_vec();
    let q: usize = ql[0].parse().unwrap();
    let l: usize = ql[1].parse().unwrap();

    let mut stack = VecDeque::new();
    let mut len = 0;

    for _ in 0..q {
        let query = read_vec();

        if query[0] == "Push" {
            let n: usize = query[1].parse().unwrap();
            let m: i64 = query[2].parse().unwrap();
            if len + n > l {
                println!("FULL");
                return;
            }
            stack.push_back((n, m));
            len += n;
        }

        if query[0] == "Pop" {
            let mut n: usize = query[1].parse().unwrap();
            if n > len {
                println!("EMPTY");
                return;
            }
            len -= n;

            while n > 0 {
                let (kn, km) = stack.pop_back().unwrap();
                let c = std::cmp::min(kn, n);
                n -= c;

                if kn > c {
                    stack.push_back((kn - c, km));
                }
            }
        }

        if query[0] == "Top" {
            if len == 0 {
                println!("EMPTY");
                return;
            }
            println!("{}", stack[stack.len() - 1].1);
        }

        if query[0] == "Size" {
            println!("{len}");
        }

        // println!("{stack:?}");
    }

    println!("SAFE");
}
