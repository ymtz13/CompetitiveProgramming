fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let h: usize = read_line().parse().unwrap();

    let mut r = 0;
    for d in 0..50 {
        if r > h {
            println!("{d}");
            return;
        }

        r += 1 << d;
    }
}
