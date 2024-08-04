fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn read_vec() -> Vec<usize> {
    read_line().split_whitespace().map(|c| c.parse().unwrap()).collect()
}

fn read_uu() -> (usize, usize) {
    let uu = read_vec();
    (uu[0], uu[1])
}

fn main() {
    let n: usize = read_line().parse().unwrap();

    let mut ev = vec![];
    for _ in 0..n {
        let (l, r) = read_uu();

        ev.push(l * 2);
        ev.push(r * 2 + 1);
    }
    ev.sort();

    let mut cnt: usize = 0;
    let mut ans: usize = 0;

    for &v in &ev {
        if v % 2 == 0 {
            ans += cnt;
            cnt += 1;
        } else {
            cnt -= 1;
        }
    }

    println!("{ans}");
}
