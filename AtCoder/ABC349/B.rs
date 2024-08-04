fn read_line() -> String {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    String::from(s.trim())
}

fn main() {
    let s: Vec<_> = read_line().bytes().collect();
    let mut cnt = vec![0; 200];

    for &c in &s {
        cnt[c as usize] = s.iter().filter(|&v| *v == c).count();
    }

    // println!("{:?}", cnt);

    let mut ans = "Yes";
    for i in 1..=s.len() {
        let mut x = 0;
        for &c in &cnt {
            if c == i {
                x += 1;
            }
        }
        if x != 0 && x != 2 {
            ans = "No"
        }
    }

    println!("{}", ans);
}
