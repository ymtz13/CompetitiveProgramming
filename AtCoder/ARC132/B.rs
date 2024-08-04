fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|v| v.parse().unwrap()).collect()
}

fn main() {
    let n = read_vec()[0];
    let pp = read_vec();

    let mut i_1 = 0;
    let mut i_n = 0;
    for i in 0..n {
        if pp[i] == 1 {
            i_1 = i + 1;
        }
        if pp[i] == n {
            i_n = i + 1;
        }
    }

    use std::cmp::min;

    if i_1 + 1 == i_n {
        if n == 2 {
            println!("0");
            return;
        }

        println!("{}", 1 + min(i_1, n - i_n + 1));
        return;
    }

    if i_1 == i_n + 1 {
        if n == 2 {
            println!("1");
            return;
        }

        println!("{}", min(i_n, n - i_1 + 3));
        return;
    }

    if i_1 == 1 {
        println!("0");
    } else {
        println!("1");
    }
}
